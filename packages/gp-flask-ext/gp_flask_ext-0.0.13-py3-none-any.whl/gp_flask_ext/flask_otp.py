import os
import pyotp
from loguru import logger
from flask import Blueprint, Flask, request, render_template, session, redirect, url_for

__all__ = ["init_app"]

def init_app(app: Flask, config=None):
    # Merge the default config with the provided config
    base_config = app.config.get("OTP_CONFIG", {})
    if config:
        base_config.update(config)
    config = base_config
    secret = os.getenv("OTP_SECRET")        # 1. 先从环境变量中获取密钥
    secret = config.get("secret", secret)   # 2. 再从配置文件中获取密钥
    if not secret:
        logger.error("Secret is required for OTP generation.")
        return
    if isinstance(secret, str):         # 支持单个用户简易配置
        secrets = [("admin", secret)]
    if isinstance(secret, list):        # 支持多个用户, 第一个最好是admin
        secrets = secret

    otp = {}
    for name, secret in secrets:
        totp = pyotp.TOTP(secret)
        otp[name] = totp
    app.extensions["otp"] = totp

    if config.get("blueprint", True):
        bp_name = config.get("blueprint_name", "otp")
        bp_url_prefix = config.get("blueprint_url_prefix", "/otp")
        bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix, template_folder="templates")  # 创建一个蓝图对象
        
        @bp.route('/')
        def index():
            user = session.get("user", "")
            return render_template("otp/index.html", user=user)
        
        @bp.route('/login', methods=["POST"])
        def login():
            token = request.json.get("token")
            name = request.json.get("name", "admin")
            if not token:
                return {"error": "Token is required."}, 400
            
            if name not in otp:
                return {"error": f"Name {name} is not found."}, 400
            
            if otp[name].verify(token):
                session["user"] = name
                
                next_page = session.pop('next', None)  # 获取记录的原始页面
                return {
                    "message": "Login successful",
                    "next": next_page or "/"
                }
            
            return "Login failed", 401
        
        @bp.route('/logout', methods=["POST", "GET"])
        def logout():
            session.pop("user", None)
            return "Logout successful"
                
        # 定义忽略登录检查的路由列表
        whitelist = config.get("whitelist", [])
        whitelisted_routes = [f'{bp_name}.login', f'{bp_name}.index', 'static']
        whitelisted_routes.extend(whitelist)

        if config.get("check_session", True):
            @app.before_request
            def check_user_session():
                # 如果当前路由在忽略检查列表中，则不做任何处理
                if request.endpoint in whitelisted_routes:
                    return

                # 检查用户是否已登录
                if 'user' not in session:
                    # 存储用户想访问的原始页面（使用 request.path 获取当前请求路径）
                    session['next'] = request.path
                    return redirect(url_for(f'{bp_name}.index'))

        app.register_blueprint(bp)  # 注册蓝图
        logger.info("Registered the OTP blueprint")
