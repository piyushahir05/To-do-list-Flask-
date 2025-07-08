from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#create database object globallly
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs(app.instance_path, exist_ok=True)

    app.config['SECRET_KEY']='your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(app.instance_path,'todo.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app