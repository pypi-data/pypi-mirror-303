import time
import json
import threading
from datetime import datetime, timezone
from loguru import logger
from celery import Celery
from celery.events.state import Task, states, Worker
from celery.result import AsyncResult
from celery.events import EventReceiver
from .nocodb import NocodbClient


class Monitor(threading.Thread):

    def __init__(self, app:Celery, nocodb: NocodbClient):
        threading.Thread.__init__(self)
        self.name = "MonitorThread"
        self.app = app
        self.state = app.events.State()         # celery 内部 in-memory 状态
        
        # nocodb 相关
        self.nocodb = nocodb
        self.tables = self.nocodb.get_tables()
        self.worker_table_id = self.tables["Worker"]
        self.task_table_id = self.tables["Task"]
        self.queue_table_id = self.tables["Queue"]
        self._queues_cache = { q["Title"]:q for q in self.list_queues().get("list") }     # queue_name : queue_object
        self.task_link_columns = self.nocodb.get_table_links(self.task_table_id)        # task表的link字段
        
        self.should_stop = False
        self.daemon = True
        self._uuid_cache = {}        # 缓存uuid和nocodb中的Id
        self._update_task_lock = threading.Lock()
        
        # 巡检 pending task, 避免worker更新了状态, 但是Monitor未收到消息的情况
        self.check_interval = 60
        self.check_thread = threading.Thread(target=self.run_check, name="CheckThread")
        self.check_thread.setDaemon(True)
        self.check_thread.start()
        logger.info("Celery event monitor main thread started")

    def list_queues(self):
        """
        查询队列列表
        """
        return self.nocodb.get(self.queue_table_id, limit=10000)

    def list_results(self, name=None, state=None, offset=0, limit=25):
        """
        查询任务列表
        """
        where = []
        if name: where.append(f"(name,eq,{name})")
        if state: where.append(f"(state,eq,{state})")
        # ref: https://data-apis-v2.nocodb.com/#tag/Table-Records/operation/db-data-table-row-list
        params = {
            "where": "~and".join(where),
            "sort": "-timestamp"        # 默认倒序
        } 
        logger.debug("querying {}...", params)
        return self.nocodb.get(self.task_table_id, params=params, offset=offset, limit=limit)

    def add_new_result_to_nocodb(self, record: dict):
        """新增任务到 nocodb, 并将 uuid 缓存到本地
    
        主要为了处理PENDING状态task信息不入库的问题
        record: dict
            {
                "task_id": "task_id",
                "name": "task_name",
                "args": [],
                "kwargs": {},
                "state": "PENDING",
                "queue": ""
            }
        """
        resp = self._add_or_update_task_to_nocodb(record)
        if "queue" in record:
            queue_name = record["queue"]
            record["Queue"] = self._queues_cache.get(queue_name)
        link_field_id = self.task_link_columns.get("Queue")
        self.nocodb.link(self.task_table_id, link_field_id, resp["Id"], record["Queue"])
        return resp

    def _add_worker_to_nocodb(self, worker):
        """worker schema in nocodb
        {
            'hostname': 'worker@notmmao', 'utcoffset': -8, 
            'pid': 24076, 'clock': 9, 'freq': 2.0, 'active': 0, 
            'processed': 0, 'loadavg': [0.0, 0.0, 0.0], 
            'sw_ident': 'py-celery', 'sw_ver': '5.2.7', 'sw_sys': 'Windows', 
            'timestamp': 1728550831.797462, 'local_received': 1728550831.8085027,
            'type': 'worker-offline', 
        }
        """
        # worker.pop("local_received")
        if "timestamp" in worker:
            worker["timestamp"] = datetime.fromtimestamp(worker["timestamp"], tz=timezone.utc).isoformat()
        if "local_received" in worker:
            worker["local_received"] = datetime.fromtimestamp(worker["local_received"], tz=timezone.utc).isoformat()
        self.nocodb.add_one(self.worker_table_id, worker, key="hostname", update_if_exists=True)

    def _add_result_to_nocodb(self, task: Task):
        """
        将任务添加到 NocoDB 中。

        此方法将任务记录添加到 NocoDB 数据库中。如果任务已经存在，则更新现有记录。

        参数:
            task (Task): 要添加或更新的任务对象。

        返回:
            dict: 包含 NocoDB 响应的字典。

        记录结构:
            - task_id: 任务的唯一标识符
            - name: 任务名称
            - state: 任务状态
            - result: 任务结果
            - args: 任务参数
            - kwargs: 任务关键字参数
            - exception: 任务异常信息
            - traceback: 任务异常追踪
            - timestamp: 任务时间戳
            - eta: 任务预计执行时间
            - retries: 任务重试次数
            - worker: 执行任务的工作节点

        如果任务记录已经存在，使用任务 ID 从缓存中获取记录 ID 并更新记录。
        否则，添加新记录并将记录 ID 缓存起来。
        """
        record = {
            "task_id": task.id,
            "name": task.name,
            "state": task.state,
            "result": task.result,
            "args": task.args,
            "kwargs": task.kwargs,
            "exception": task.exception,
            "traceback": task.traceback,
            "timestamp": task.timestamp,
            # "worker": repr(task.worker),
            "eta": task.eta,
            "retries": task.retries,
        }
        if task.state == states.SUCCESS:
            ar:AsyncResult = self.app.AsyncResult(task.id)
            record["result"] = json.dumps(ar.result)        # 获取完整的结果
            if ar.queue:
                record["queue"] = ar.queue
        if task.worker:
            # celery.events.state.Worker
            record["worker"] = repr(task.worker)
        return self._add_or_update_task_to_nocodb(record)
        
    def _add_or_update_task_to_nocodb(self, record:dict):
        """
        将任务记录添加到 NocoDB 数据库中。
        如果任务记录已经存在，使用任务 ID 从缓存中获取记录 ID 并更新记录。
        否则，添加新记录并将记录 ID 缓存起来。
        
        此函数加了锁, 所有更新task的操作都应该调用次函数, 以避免多线程冲突.
        """
        with self._update_task_lock:
            task_id = record["task_id"]
            if "timestamp" in record:
                record["timestamp"] = datetime.fromtimestamp(record["timestamp"], tz=timezone.utc).isoformat()
            record_id = self._uuid_cache.get(task_id)
            if record_id:
                record["Id"] = record_id
                resp = self.nocodb.update(self.task_table_id, record)
                logger.debug("update task {} to nocodb", record)
            else:
                resp = self.nocodb.add_one(self.task_table_id, record, key="task_id", update_if_exists=True)
                logger.debug("add task {} to nocodb", record)
                self._uuid_cache[task_id] = resp["Id"]
            return resp
        

    def check_pending_tasks(self):
        task_list = self.nocodb.get(self.task_table_id, params={"where": "(state,eq,PENDING)"}).get("list")
        logger.debug("Checking pending tasks {}...")
        for task in task_list:
            if "task_id" not in task: continue  # 排除虚拟/测试任务记录
            ar:AsyncResult = self.app.AsyncResult(task["task_id"])
            
            if ar.state != states.PENDING:
                # 状态变化才更新任务记录
                record = {
                    "task_id": task["task_id"],
                    "state": ar.state,
                    # "result": ar.result
                }
                if ar.state in states.EXCEPTION_STATES:
                    record["traceback"] = ar.traceback
                    record["exception"] = str(ar.result)
                else:
                    record["result"] = ar.result
                logger.info("Task {} is in state {} result.result={}", task["task_id"], ar.state, ar.result)
                self._add_or_update_task_to_nocodb(record)

    def run_check(self):
        while not self.should_stop:
            try:
                self.check_pending_tasks()
            except Exception as e:
                logger.error("Error in {}: {}, retrying...", self.check_thread.name, e)
            finally:
                time.sleep(self.check_interval)

    def run(self):
        while not self.should_stop:
            try:
                self._run()
            except Exception as e:
                logger.error("Error in {}: {}, retrying...", self.name, e)
                continue

    def _run(self):
        with self.app.connection() as connection:
            recv : EventReceiver = self.app.events.Receiver(connection, handlers={
                'task-send': self.on_task_event,
                'task-received': self.on_task_event,
                'task-started': self.on_task_event,
                'task-progress': self.on_task_event_custom,    # 自定义处理进度
                'task-succeeded': self.on_task_event,
                'task-failed': self.on_task_event,
                'task-rejected': self.on_task_event,
                'task-revoked': self.on_task_event,
                'task-retried': self.on_task_event,
                'worker-online': self.on_worker_event,
                'worker-offline': self.on_worker_event,
                'worker-heartbeat': self.on_worker_event,
                # 'worker-heartbeat': self.state.event,   # 默认处理程序
                '*': self.state.event,   # 默认处理程序
            })
            logger.info("Celery event Monitor thread connected to broker")
            recv.capture(limit=None, timeout=None, wakeup=True)

    def on_worker_event(self, event):
        self.state.event(event)
        logger.debug(f"Worker: event {event}")
        self._add_worker_to_nocodb(event)

    def on_task_event_custom(self, event):
        self.state.event(event)
        logger.debug("Task: event {}", event)
        if 'uuid' not in event:
            logger.warning("Task event without uuid {}", event)
            return
        if event['type'] == 'task-progress':
            # 自定义处理进度
            record = {
                "task_id": event["uuid"],
                "meta": json.dumps(event.get("meta", {})),
                "state": event["state"]
            }
            return self._add_or_update_task_to_nocodb(record)

    def on_task_event(self, event):
        self.state.event(event)
        task: Task = self.state.tasks.get(event['uuid'])
        self._add_result_to_nocodb(task)
        if task.state in states.EXCEPTION_STATES:
            logger.warning(f"Task: {task.state} {task.info()}")
        else:
            logger.debug(f"Task: {task.state} {task.info()}")
            
