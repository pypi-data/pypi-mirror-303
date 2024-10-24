import os
import json
import time
from loguru import logger
from flask import Blueprint, Flask, request, Response, render_template, jsonify
from .mqtt import MqttClient

def init_app(app: Flask, config: dict):
    # Check if the provided config is valid
    if not (config is None or isinstance(config, dict)):
        raise ValueError("`config` must be an instance of dict or None")

    # Merge the default config with the provided config
    base_config = app.config.get("MQTT_CONFIG", {})
    if config:
        base_config.update(config)
    config = base_config

    if config.get("tls", False):
        # Check if the provided paths are absolute, if not, make them absolute using the instance path
        instance_path = app.instance_path
        ca_certs = config.get("ca_certs", "ca.crt")
        client_certs = config.get("client_certs", "client.crt")
        client_key = config.get("client_key", "client.key")
        if not os.path.isabs(ca_certs):
            config['ca_certs'] = f"{instance_path}/{ca_certs}"
        if not os.path.isabs(client_certs):
            config['client_certs'] = f"{instance_path}/{client_certs}"
        if not os.path.isabs(client_key):
            config['client_key'] = f"{instance_path}/{client_key}"

    _mqtt = MqttClient(app, config)
    ext_name = config.get("ext_name", "mqtt")
    app.extensions[ext_name] = _mqtt
    logger.info("Initialized the MqttClient")
    
    if config.get("blueprint", True):
        bp_name = base_config.get("blueprint_name", "mqtt")
        bp_url_prefix = base_config.get("blueprint_url_prefix", "/mqtt")
        bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix, template_folder="templates")  # 创建一个蓝图对象

        # Register the blueprint
        @bp.route("/test", methods=["GET"])
        def test():
            return config
        
        @bp.route("/publish", methods=["GET", "POST"])
        def publish():
            if request.method == "POST":
                data = request.get_json()
                topic = data.get("topic")
                payload = data.get("payload")
            else:
                topic = request.args.get("topic")
                payload = request.args.get("payload")
            _mqtt.publish(topic, payload)
            return f"Published message to {topic}: {payload}"
        
        @bp.route("/subscribe", methods=["GET", "POST"])
        def subscribe():
            if request.method == "POST":
                data = request.get_json()
                topic = data.get("topic")
            else:
                topic = request.args.get("topic")
            r = _mqtt.mqtt.subscribe(topic, _mqtt.qos)
            logger.debug(f"Subscribed to {topic}: {r}")
            return f"Subscribed to {topic}"
        
        @bp.route('/sessions', methods=["GET"])
        def sessions():
            _sessions = [s.to_dict() for s in _mqtt.sessions.values()]
            return jsonify(_sessions)
        
        @bp.route('/session/<tag>', methods=["GET"])
        def session(tag):
            logger.debug(f"Get session: {tag}")
            if tag is None:
                return "No session tag provided"
            _session = _mqtt.sessions.get(tag, None)
            if _session is None:
                return f"No session with tag: {tag}"
            return jsonify(_session.to_dict())

        @bp.route('/', methods=["GET"])
        def index():
            return render_template("mqtt/index.html", topic=_mqtt.subscribe_topic)

        app.register_blueprint(bp)  # 将蓝图注册到应用程序上
        logger.info("Registered the Mqtt blueprint")

    if config.get("socketio", True):
        from flask_socketio import SocketIO
        async_mode = config.get("socketio_async_mode", "threading")
        socketio = SocketIO(app, async_mode=async_mode)
        _mqtt.socketio = socketio

        @socketio.on('connect')
        def test_connect():
            logger.debug('Client connected')
            
        @socketio.on('disconnect')
        def test_disconnect():
            logger.debug('Client disconnected')