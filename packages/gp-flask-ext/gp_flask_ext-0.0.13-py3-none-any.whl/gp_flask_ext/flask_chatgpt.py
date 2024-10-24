import os
from openai import OpenAI, AzureOpenAI
from loguru import logger
from flask import Blueprint, Flask, request, render_template, jsonify
from .nocodb import NocodbClient

__all__ = ["init_app"]

default_config = {
    "api_key": os.getenv("OPENAI_API_KEY"),
    "base_url": os.getenv("OPENAI_BASE_URL"),
    "api_version": os.getenv("OPENAI_API_VERSION"),
    "api_type": os.getenv("OPENAI_API_TYPE"),
    "model": os.getenv("OPENAI_MODEL"),
    "ext_name": "chatgpt",
    "blueprint": True,
    "blueprint_name": "chatgpt",
    "blueprint_url_prefix": "/chatgpt",
}

def init_app(app: Flask, config={}):
    # Merge the default config with the provided config
    default_config.update(config)
    base_config = app.config.get("CHATGPT_CONFIG", {})
    default_config.update(base_config)
    config = default_config
    
    # logger.info(config)
    
    model = config.get("model")
    api_type = config.get("api_type")
    if api_type == "azure":
        client = AzureOpenAI(
            api_key=config.get("api_key"),
            base_url=config.get("base_url"),
            api_version=config.get("api_version"),
        )
    else:
        client = OpenAI(
            api_key=config.get("api_key"),
            base_url=config.get("base_url"),
        )
    ext_name = config.get("ext_name", "chatgpt")
    app.extensions[ext_name] = client

    if config.get("blueprint", True):
        bp_name = config.get("blueprint_name", "chatgpt")
        bp_url_prefix = config.get("blueprint_url_prefix", "/chatgpt")
        bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix, template_folder="templates")  # 创建一个蓝图对象
        
        # Initialize the storage client
        storage = None
        table_id = None
        storage_config = config.get("storage")
        if storage_config:
            storage_type = storage_config.get("type")
            if storage_type == "nocodb":
                storage = NocodbClient(**storage_config)
                table_id = storage_config.get("table_id")
                logger.info("Initialized the storage client table_id: {}", table_id)
        @logger.catch
        def save_chat_record(chat_id, user_input, message, model):
            if storage:
                storage.add_one(table_id, {
                    "chat_id": chat_id,
                    "user_input": user_input,
                    "message": message,
                    "model": model,
                }, key="chat_id")

        @bp.route('/')
        def index():
            return render_template("chatgpt/index.html", max_tokens=1600)
        
        @bp.route('/models')
        def models():
            if model:
                # 如果手动制定了model, 直接返回
                return {"data": [{"id": model}]}    # 保持统一schema
            return client.models.list().dict()
        
        @bp.route('/ask', methods=["POST"])
        def ask():
            user_input = request.json.get("user_input")
            max_tokens = request.json.get("max_tokens")
            model = request.json.get("model")
            logger.debug("[{}]{}", max_tokens, user_input)
            if not user_input:
                return {"error": "User input is required."}, 400
            data = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                "max_tokens": max_tokens,
                "model": model,
                "temperature": 0.5,
                "top_p": 1.0,
                "frequency_penalty": 0.0,
                "presence_penalty": 0.,
                "stream": False
            }

            response = client.chat.completions.create(
                **data
            )
            # for chunk in response:
            #     message = chunk.choices[0].delta.content or ""
            message = response.choices[0].message.content or ""
            save_chat_record(response.id, user_input, message, model)
            return message

        app.register_blueprint(bp)  # 注册蓝图
        logger.info("Registered the ChatGPT blueprint")
