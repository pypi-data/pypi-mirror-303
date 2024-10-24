import os
import base64
from loguru import logger
from flask import Blueprint, Flask, request, Response, render_template, jsonify
from .protobuf import ProtobufLoader

def init_app(app: Flask, config: dict):
    # Check if the provided config is valid
    if not (config is None or isinstance(config, dict)):
        raise ValueError("`config` must be an instance of dict or None")

    # Merge the default config with the provided config
    base_config = app.config.get("PROTOBUF_CONFIG", {})
    if config:
        base_config.update(config)
    config = base_config

    # Check if the provided path is absolute, if not, make it absolute using the instance path
    path = config.get("path", "protobuf")
    if not os.path.isabs(path):
        path = os.path.join(app.instance_path, path)
    
    pb_loader = ProtobufLoader(path)
    pb_loader.load()
    ext_name = config.get("ext_name", "pb_loader")
    app.extensions[ext_name] = pb_loader
    logger.info("Initialized the ProtobufLoader")
    
    if config.get("blueprint", True):
        bp_name = base_config.get("blueprint_name", "pb")
        bp_url_prefix = base_config.get("blueprint_url_prefix", "/pb")
        bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix, template_folder="templates")  # 创建一个蓝图对象

        # Register the blueprint
        @bp.route("/", methods=["GET"])
        def index():
            return render_template("protobuf/index.html")
        
        @bp.route("/test", methods=["GET"])
        def test():
            return config
        
        @bp.route("/filelist", methods=["GET"])
        def filelist():
            """返回当前模块的所有文件"""
            return pb_loader.filelist()
        
        @bp.route("/schema", methods=["GET"])
        def schema():
            """返回当前模块的版本和所有的属性"""
            pb = request.args.get("pb")
            return pb_loader.schemas.get(pb, {})
        
        @bp.route("/schemas", methods=["GET"])
        def schemas():
            """返回当前模块的版本和所有的属性"""
            return pb_loader.schemas
        
        @bp.route("/raw", methods=["GET"])
        def raw():
            """返回原始的 pb 文件内容"""
            pb = request.args.get("pb")
            code = pb_loader.proto_files_dict.get(pb, "")
            return "<pre><code>{}<code></pre>".format(code)
        
        @bp.route("/encode", methods=["POST"])
        def encode():
            """编码"""
            data = request.get_json()
            proto_file = data.get("proto_file")
            message_name = data.get("message_name")
            payload = data.get("payload")

            if not proto_file or not message_name:
                return "Invalid parameters", 400
            data = pb_loader.encode(proto_file, message_name, payload)
            return data

        @bp.route("/decode", methods=["POST"])
        def decode():
            """解码"""
            data = request.get_json()
            proto_file = data.get("proto_file")
            message_name = data.get("message_name")
            payload_type = data.get("payload_type", "base64")
            payload = data.get("payload")

            if payload_type == "base64":
                payload = base64.decodebytes(payload.encode())
                logger.info(payload)

            if not proto_file or not message_name:
                return "Invalid parameters", 400
            data = pb_loader.decode(proto_file, message_name, payload)
            return data

        app.register_blueprint(bp)  # 将蓝图注册到应用程序上
        logger.info("Registered the Protobuf blueprint")