import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data/test.db")}'
