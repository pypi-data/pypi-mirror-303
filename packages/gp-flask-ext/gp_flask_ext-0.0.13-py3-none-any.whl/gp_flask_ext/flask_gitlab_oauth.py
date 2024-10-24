import os
import requests
from loguru import logger
from urllib.parse import urlencode
from flask import Flask, Blueprint, redirect, session, request, jsonify, url_for

bp = Blueprint("auth", __name__)
CONFIG = {
    "OAUTH_DOMAIN" : os.environ.get("GITLAB_DOMAIN"),
    "OAUTH_AUTHORIZE_URL": "/oauth/authorize",
    "OAUTH_TOKEN_URL": "/oauth/token",
    "OAUTH_USER_URL": "/api/v4/user",
    "OAUTH_CLIENT_ID": os.environ.get("GITLAB_CLIENT_ID"),
    "OAUTH_CLIENT_SECRET": os.environ.get("GITLAB_CLIENT_SECRET"),
    "OAUTH_TOKEN": None,
}

def init_app(app: Flask, config=None):
    app.register_blueprint(bp, url_prefix="/auth")
    logger.info("Registered the auth blueprint")

    if config and isinstance(config, dict):
        CONFIG.update(config)

def get_access_token(code, redirect_uri):
    base_url = f"https://{CONFIG['OAUTH_DOMAIN']}" + CONFIG["OAUTH_TOKEN_URL"]
    params = {
        'code': code,
        'client_id': CONFIG["OAUTH_CLIENT_ID"],
        'client_secret': CONFIG["OAUTH_CLIENT_SECRET"],
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri
    }
    resp = requests.post(base_url, data=params).json()
    return resp

def get_user(access_token):
    base_url = f"https://{CONFIG['OAUTH_DOMAIN']}" + CONFIG["OAUTH_USER_URL"]
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    resp = requests.get(base_url, headers=headers).json()
    return resp

@bp.route("/login")
def login():
    redirect_uri = url_for('auth.login', _external=True)
    OAUTH_DOMAIN = CONFIG["OAUTH_DOMAIN"]
    if request.args.get("code", False):
        code = request.args.get("code")

        resp = get_access_token(code, redirect_uri)
        CONFIG["OAUTH_TOKEN"] = resp['access_token']
        user = get_user(CONFIG["OAUTH_TOKEN"])
        
        session['user'] = user
        return jsonify({"code": code, "user": user})
    else:
        base_url = f"https://{OAUTH_DOMAIN}" + CONFIG["OAUTH_AUTHORIZE_URL"]
        params = {
            'redirect_uri': redirect_uri,
            'client_id': CONFIG["OAUTH_CLIENT_ID"],
            'scope': 'read_api',
            'response_type': 'code',
            'extra_params': {'approval_prompt': ''},
        }
        oauth_url = base_url + '?' + urlencode(params)
        return redirect(oauth_url)
    
@bp.route("/logout")
def logout():
    session.pop('user', None)
    return redirect('/')