from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import app_config
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	db.init_app(app)

	@app.route('/')
	def hello_world():
		return 'Hello, World!'

	login_manager.init_app(app)
	login_manager.login_message="Must be logged in to access this page."
	login_manage.login_view = "auth.login"

	return app
