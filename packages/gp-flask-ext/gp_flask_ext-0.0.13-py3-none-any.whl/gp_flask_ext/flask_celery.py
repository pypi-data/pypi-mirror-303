import time
import json
import inspect
from flask import Flask, Blueprint, request, render_template
from celery import Celery, Task, shared_task, states
from celery.result import AsyncResult
from loguru import logger
from .celery_events import Monitor
from .nocodb import NocodbClient

@shared_task
def hello():
    return "Hello, World!"

def get_default_value(param_type):
    """根据参数类型生成默认值"""
    if param_type == 'int':
        return 0
    elif param_type == 'float':
        return 0.0
    elif param_type == 'str':
        return ''
    elif param_type == 'bool':
        return False
    elif param_type == 'list':
        return []
    elif param_type == 'dict':
        return {}
    else:
        return None  # 无法识别的类型，设为 None

def get_task_signature(task):
    sig = inspect.signature(task)
    params = {}
    default_kwargs = {}

    for name, param in sig.parameters.items():
        # 获取参数类型
        if param.annotation != inspect.Parameter.empty:
            if hasattr(param.annotation, '__name__'):
                param_type = param.annotation.__name__
            else:
                param_type = str(param.annotation)
        else:
            param_type = None

        # 根据类型生成默认值，如果没有默认值，则使用类型推断的默认值
        if param.default != inspect.Parameter.empty:
            default_value = param.default
        else:
            default_value = get_default_value(param_type)

        params[name] = {
            'default': default_value,
            'kind': str(param.kind),
            'type': param_type
        }
        
        # 将默认值放入 kwargs
        default_kwargs[name] = default_value

    return {'signature': params, 'kwargs': default_kwargs}

def init_app(app: Flask, config=None) -> Celery:
    # Check if the provided config is valid
    if not (config is None or isinstance(config, dict)):
        raise ValueError("`config` must be an instance of dict or None")

    # Merge the default config with the provided config
    base_config = app.config.get("CELERY_CONFIG", {})
    if config:
        base_config.update(config)
    config = base_config

    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(config)
    celery_app.set_default()
    
    ext_name = config.get("ext_name", "celery")
    app.extensions[ext_name] = celery_app
    logger.info("Initialized the Celery app")
    monitor = None

    # 监听事件
    if config.get("enable_events", True):
        nocodb_config = config.get("nocodb")
        nocodb = NocodbClient(**nocodb_config)
        monitor = Monitor(celery_app, nocodb)
        monitor.start()

    if config.get("blueprint", True):
        # Register the blueprint
        bp_name = config.get("blueprint_name", "celery")
        bp_url_prefix = config.get("blueprint_url_prefix", "/celery")
        bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix, template_folder="templates")
        ins = celery_app.control.inspect()

        def safe_result(result):
            "returns json encodable result"
            try:
                json.dumps(result)
            except TypeError:
                return repr(result)
            return result
        
        def _inspect_object_2_list(o):
            ret = []
            if o:
                _id = 0
                for key, value in o.items():
                    ret.append({
                        "id": _id,
                        "worker": key,
                        "value" : value
                    })
                    _id += 1
            return ret
        
        @bp.route("/")
        def index():
            return render_template("celery/index.html")
        
        @bp.route("/inspect")
        def inspect():
            return render_template("celery/inspect.html")
        
        @bp.route("/inspect/stats")
        def inspect_stats():
            o = ins.stats()      # 返回值是字典，键是worker名字，值是状态, dict类型
            return _inspect_object_2_list(o)
        
        @bp.route("/inspect/active")
        def inspect_active():
            o = ins.active()            # 返回值是字典，键是worker名字，值是当前活动任务列表, list类型
            return _inspect_object_2_list(o)
        
        @bp.route("/inspect/queues")
        def inspect_queues():
            o = ins.active_queues()     # 返回值是字典，键是worker名字，值是队列列表, list类型
            return _inspect_object_2_list(o)
        
        @bp.route("/inspect/memsample")
        def inspect_memsample():
            o = ins.memsample()         # 返回值是字典，键是worker名字，值是内存占用情况, dict类型
            return _inspect_object_2_list(o)
        
        @bp.route("/inspect/conf")
        def inspect_conf():
            o = ins.conf()              # 返回值是字典，键是worker名字，值是配置信息, dict类型
            return _inspect_object_2_list(o)
        
        @bp.route("/inspect/clock")
        def inspect_clock():
            o = ins.clock()             # 返回值是字典，键是worker名字，值是时钟信息, dict类型
            return _inspect_object_2_list(o)
        
        @bp.route("/inspect/registered")
        def inspect_registered():
            o = ins.registered()        # 返回值是字典，键是worker名字，值是已注册的任务列表, list类型
            return _inspect_object_2_list(o)
        
        @bp.route("/inspect/report")
        def inspect_report():
            o = ins.report()            # 返回值是字典，键是worker名字，值是报告信息, dict类型
            return _inspect_object_2_list(o)
        
        @bp.route("/inspect/ping")
        def inspect_ping():
            o = ins.ping()              # 返回值是字典，键是worker名字，值是PING响应信息, dict类型
            return _inspect_object_2_list(o)

        @bp.route("/tasks")
        def tasks():
            tasks_info = []
            for task_name, task in celery_app.tasks.items():
                if task_name.startswith('celery.'):  # 跳过系统任务
                    continue
                # 获取任务签名
                task_signature = get_task_signature(task)
                tasks_info.append({
                    'name': task_name,
                    'signature': task_signature["signature"],
                    'kwargs': task_signature["kwargs"],
                    'doc': task.__doc__,
                    'task_name': task.__name__,
                })
            return tasks_info
            # return {"tasks": [task.name for task in celery_app.tasks.values() if not task.name.startswith("celery.")]}

        @bp.route("/tasks/states")
        def state():
            return [state for state in states.__all__]


        @bp.route("/tasks/send", methods=["POST"])
        def send():
            data = request.json
            if not data:
                return {"error": "No data provided"}, 400

            taskname = data.get("name")
            if not taskname:
                return {"error": "No task name provided"}, 400
            args = data.get("args", [])
            kwargs = data.get("kwargs", {})
            queue = data.get("queue")
            countdown = int(data.get("countdown", 0))
            eta = data.get("eta")

            options = {}        # celery send_task 调用可选项
            if queue: options['queue'] = queue
            if countdown: options['countdown'] = countdown
            if eta: 
                options['eta'] = eta
                options.pop('countdown')    # eta 优先级高于 countdown, 
                
            result:AsyncResult = celery_app.send_task(
                taskname, args=args, kwargs=kwargs, **options)
            task_info = {
                "task_id": result.task_id, 
                "name": taskname, 
                "state": result.state,
                "args": args,
                "kwargs": kwargs,
                "queue": queue,
                "timestamp": time.time(),
            }
            if monitor:
                monitor.add_new_result_to_nocodb(task_info)
            return task_info
        
        @bp.route("/results")
        def results():
            name = request.args.get("name")
            state = request.args.get("state")
            offset = int(request.args.get("offset", 0))
            limit = int(request.args.get("limit", 25))
            return monitor.list_results(name=name, state=state, offset=offset, limit=limit)

        @bp.route("/results/<task_id>")
        def result(task_id):
            result: AsyncResult = celery_app.AsyncResult(task_id)
            logger.info(f"Task {task_id} is in state {result.state} result.result={result.result}")
            response = {"task_id": task_id, "state": result.state}

            if result.state == states.FAILURE:
                response.update({'result': safe_result(result.result),
                                'traceback': result.traceback})
            else:
                response.update({'result': safe_result(result.result)})

            return response

        @bp.route("/queues")
        def queues():
            if monitor: return monitor.list_queues()
            return "No monitor", 500

        @bp.route("/test")
        def test():
            return {
                "broker": celery_app.conf.broker_url,
                "result_backend": celery_app.conf.result_backend,
            }

        app.register_blueprint(bp)
        logger.info("Registered the Celery blueprint")

    return celery_app
