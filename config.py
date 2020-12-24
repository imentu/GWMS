import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = b'\xc0\x0c\xb5t\x17rgN\xce\x03\xe4\xeeVr\xe5E'  # 配置后端 cookie 加密序列
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data/sys.db")}'  # 配置数据库地址
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    FLASK_ADMIN_SWATCH = 'cerulean'

    CKEDITOR_PKG_TYPE = 'basic'
    CKEDITOR_SERVE_LOCAL = True


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
