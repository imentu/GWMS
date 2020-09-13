import os
from common import basedir


class Config(object):
    SECRET_KEY = b'\xc0\x0c\xb5t\x17rgN\xce\x03\xe4\xeeVr\xe5E'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data/sys.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
