import os

from flask import Flask,session
from flask.cli import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary
from authlib.integrations.flask_client import OAuth
from app.utils.vnd import vnd


db = SQLAlchemy()
login_manager = LoginManager()



cloudinary.config(
    cloud_name= 'dkatgavs4',
    api_key='769513968994667',
    api_secret= 'oNIu8AMfcmwLlkhANlyCYXI40B0'
)



def create_app():
    app = Flask(__name__)

    app.jinja_env.filters['vnd'] = vnd
    app.secret_key = "asjdahjgưGƯEGgG4252#adsd"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/app?charset=utf8mb4"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PAGE_SIZE"] = 4;

    db.init_app(app)

    login_manager.init_app(app)

    @app.before_request
    def check_maintenance():
        # Ví dụ: chặn toàn bộ site nếu bật maintenance
        if app.config.get("MAINTENANCE_MODE"):
            return "Server đang bảo trì!", 503


    return app
load_dotenv()
oauth = OAuth(create_app())

google = oauth.register(
    name='google',
    client_id= 'xxxxx',
    client_secret='xxxxxxx',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)