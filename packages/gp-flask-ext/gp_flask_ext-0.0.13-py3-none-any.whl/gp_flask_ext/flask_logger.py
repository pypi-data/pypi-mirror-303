import sys
from loguru import logger
from flask import Blueprint, Flask, request, render_template

__all__ = ["init_app"]


def _as_dict():
    logger_core = logger._core   # 这里不得已使用了私有变量
    no2level = {v.no:k  for k,v in logger_core.levels.items()}
    for h in logger_core.handlers.values():
        levelno = h.levelno
        if levelno in no2level:
            level = no2level[levelno]
        else:
            level = "UNKNOWN"

        yield {
            "id": h._id,
            "name": h._name,
            "level": level,
            "levelno": levelno,
            "enqueue": h._enqueue,
            # "filter": h._filter,
            "formatter": h._formatter.strip(),
            # "sink": h._sink,
        }

def init_app(app: Flask, config=None):
    base_config = app.config["LOGURU_CONFIG"]
    if config:
        base_config.update(config)
    bp_name = base_config.get("blueprint_name", "logger")
    bp_url_prefix = base_config.get("blueprint_url_prefix", "/logger")
    bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix, template_folder="templates")  # 创建一个蓝图对象

    @bp.route('/')
    def index():
        return render_template("logger/index.html")
    
    @bp.route('/default')
    def default():
        """重置为默认配置"""
        logger.configure(**base_config)
        return {"status": "ok"}

    @bp.route('/test')
    def test():
        return {"status": "ok", "handlers": list(_as_dict())}

    @bp.route('/enable')
    def enable():
        name = request.args.get("name")
        if name:
            logger.enable(name)
            return {"status": "ok"}
        return {"status": "error", "message": "name not provided"}

    @bp.route('/disable')
    def disable():
        name = request.args.get("name")
        if name:
            logger.disable(name)
            return {"status": "ok"}
        return {"status": "error", "message": "name not provided"}

    @bp.route('/add', methods=["GET", "POST"])
    def add():
        if request.method == "POST":
            filter = request.json.get("filter")
            level = request.json.get("level", "INFO")
        else:
            filter = request.args.get("filter")
            level = request.args.get("level", "INFO")
        hander = logger.add(sys.stdout, filter=filter, level=level, enqueue=True)
        return {"status": "ok", "hander": hander}

    @bp.route('/remove', methods=["GET", "DELETE"])
    def remove():
        handler_id = request.args.get("id")
        if handler_id:
            handler_id = int(handler_id)
            logger.remove(handler_id)
            return {"status": "ok"}
        return {"status": "error", "message": "id not provided"}

    app.register_blueprint(bp)  # 注册蓝图
    logger.info("Registered the Logger blueprint")
