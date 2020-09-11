import os
from common import basedir


class Config(object):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data/sys.db")}'
