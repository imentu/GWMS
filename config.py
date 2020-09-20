import os

from common import basedir


class Config(object):
    SECRET_KEY = b'\xc0\x0c\xb5t\x17rgN\xce\x03\xe4\xeeVr\xe5E'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data/sys.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    FLASK_ADMIN_SWATCH = 'cerulean'

    CKEDITOR_PKG_TYPE = 'basic'
    CKEDITOR_SERVE_LOCAL = True


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
