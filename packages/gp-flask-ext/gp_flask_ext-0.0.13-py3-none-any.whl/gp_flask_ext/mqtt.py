import time
from dataclasses import dataclass, field
from queue import Queue, Empty
from typing import List, Dict

from loguru import logger
from paho.mqtt.client import MQTTMessage, Client, MQTTv5
from flask_socketio import SocketIO, emit

@dataclass
class MqttSession:
    messages : Queue = field(default_factory=Queue)
    tag : str = "Default"
    expried : float = 0.0

    def to_dict(self):
        # Convert the Queue to a list
        messages_list = list(self.messages.queue)
        return {
            "messages": messages_list,
            "tag": self.tag,
            "expried": self.expried,
        }
    

class MqttClient:
    PROTOCOL = MQTTv5
    KEEPALIVE = 60
    QOS = 0
    PORT = 1883
    messages = Queue()
    sessions : Dict[str, MqttSession] = {}
    socketio : SocketIO = None
    mqtt: Client

    def __init__(self, app, config):
        self.config = config
        self.app = app
        self.tls = config.get("tls", False)
        self.host = config["host"]
        self.port = config.get("port", self.PORT)
        self.client_id = config["mqtt_client_id"] + str(time.time())
        self.username = config.get("username", None)
        self.password = config.get("password", None)
        self.qos = config.get("qos", self.QOS)
        self.subscribe_topic = config["topic"]
        self.echo_topic = config.get("echo_topic", None)    # 回显主题, None 表示不回显
        if self.tls:
            self.ca_certs = config["ca_certs"]
            self.client_certs = config["client_certs"]
            self.client_key = config["client_key"]

        # 创建一个 MQTT 客户端
        self.mqtt = _mqtt = Client(self.client_id, protocol=self.PROTOCOL)
        # 设置用户名和密码
        _mqtt.username_pw_set(self.username, self.password)
        # 设置用户数据
        _mqtt.user_data_set(self.app)
        # 设置 TLS
        if self.tls:
            _mqtt.tls_set(ca_certs=self.ca_certs, certfile=self.client_certs, keyfile=self.client_key)
            logger.info("TLS enabled")
        # 连接到 MQTT 服务器
        _mqtt.connect(self.host, self.port, self.KEEPALIVE)
        # 订阅主题
        _mqtt.subscribe(self.subscribe_topic, self.qos)
        # 设置回调函数
        _mqtt.on_connect = self.on_connect
        _mqtt.on_message = self.on_message
        _mqtt.on_log = self.on_log
        _mqtt.on_disconnect = self.on_disconnect
        _mqtt.on_connect_fail = self.on_connect_fail
        # 启动一个线程，用于处理网络 I/O
        _mqtt.loop_start()
        self.start_session(tag="Default", expried=3600)

    def __repr__(self):
        return f"<MqttClient {self.host}:{self.port}>"

    def publish(self, topic, payload, qos=0, retain=False):
        self.mqtt.publish(topic, payload, qos, retain)

    def on_log(self, client, userdata, level, buf):
        logger.debug("{} {}", level, buf)

    def on_message(self, client, userdata, message: MQTTMessage):
        try :
            payload = message.payload.decode()
        except Exception as e:
            # 二进制文件暂时不处理
            length = len(message.payload)
            payload = f"{length} bytes binary data"
            logger.info("on_message: {}", payload)
            
        logger.debug("message: {} {}", message.topic, payload)
        self.expried_sessions()     # 删除过期的会话
        if len(self.sessions) > 0:
            json_message = self.message_to_json(message)
            for session in self.sessions.values():
                session.messages.put(json_message)
                logger.debug("Put message to session: {}", session.tag)

            # with self.app.app_context():
            if self.socketio is not None:
                logger.debug("emit mqtt_message")
                self.socketio.emit("mqtt_message", json_message)
        
        if self.echo_topic:
            self.publish(self.echo_topic, message.payload, message.qos, message.retain)

        

    def on_connect(self, client: Client, userdata, flags, rc, properties=None):
        # client.enable_bridge_mode()
        if rc == 0:
            # 在这里重新订阅
            client.subscribe(self.subscribe_topic, self.qos)
            logger.info("Connected with result code {} {}", rc, self)
        else:
            logger.warning("Connected with result code {} {}", rc, self)

    def on_disconnect(self, client: Client, userdata, rc):
        logger.info("Disconnected with result code {}", rc)

    def on_connect_fail(self, client: Client, userdata):
        logger.warning("Connect failed with result code {}", self)

    def poll(self, tag="Default", timeout=None):
        session = self.sessions.get(tag)
        if session:
            try:
                message = session.messages.get(timeout=timeout)
            except Empty:
                return None
            return message
        return None
    
    def message_to_json(self, message: MQTTMessage):
        jo = {
            "timestamp": message.timestamp, 
            "topic": message.topic,
            "qos": str(message.qos),
            "retain": message.retain,
            "mid": message.mid,
            "properties": message.properties.json() if hasattr(message, "properties") else None,
            "payload": message.payload,
        }
        return jo
    
    def start_session(self, tag="Default", expried=60):
        if tag in self.sessions:
            session = self.sessions[tag]
            if session.expried > time.time():
                return session
            else:
                del self.sessions[tag]
        session = MqttSession()
        session.tag = tag
        session.expried = time.time() + expried
        self.sessions[tag] = session
        return session
    
    def stop_session(self, tag="Default"):
        if tag in self.sessions:
            del self.sessions[tag]
            return True
        return False
    
    def clear_sessions(self):
        self.sessions.clear()
        return True
    
    def expried_sessions(self):
        """删除过期的会话"""
        _expried = []
        for session in self.sessions.values():
            if session.expried < time.time():
                # 过期的会话, 不能在这里删除, 否则会导致遍历时出错
                _expried.append(session)
                continue

        # 删除过期的会话
        if _expried:
            for session in _expried:
                tag = session.tag
                del self.sessions[tag]

    
    def __del__(self):
        if self.mqtt is None:
            return
        self.mqtt.loop_stop()
        self.mqtt.disconnect()
        self.mqtt = None
        logger.info("Disconnected from {}", self)