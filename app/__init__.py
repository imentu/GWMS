from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

'''
    毕业生工作管理系统 GWMS (Graduate Work Management System)
    管理员可以发布招聘信息， 毕业生需要填写当前找工作状态，教师可以实时查看，可以导出当前毕业生就业情况
'''

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from app.student import bp as student_bp
    app.register_blueprint(student_bp, url_prefix='/student')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.manager import bp as manager_bp
    app.register_blueprint(manager_bp, url_prefix='/manager')

    return app


from app import models
