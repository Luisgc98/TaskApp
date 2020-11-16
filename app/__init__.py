from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_mail import Mail
from .auth import auth
from .records import record
from .models import login_manager

def create_app():
	app = Flask(__name__, template_folder='templates')
	app.config.from_object(Config)
	app.register_blueprint(auth)
	app.register_blueprint(record)
	Bootstrap().init_app(app)
	SQLAlchemy().init_app(app)
	login_manager.init_app(app)
	Moment().init_app(app)
	Mail().init_app(app)

	return app