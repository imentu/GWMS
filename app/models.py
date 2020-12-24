from flask_login import UserMixin
from sqlalchemy import text
from sqlalchemy.sql import func

from app import db, login_manager

'''
    向 ORM 提供 User 数据映射对象及 User 表结构
'''


class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(80), server_default='')
    major = db.Column(db.String(200), server_default='')
    college = db.Column(db.String(200), server_default='')
    gender = db.Column(db.Integer, nullable=False, server_default=text('0'))
    type = db.Column(db.Integer, nullable=False, server_default=text('0'))
    status = db.Column(db.Integer, nullable=False, server_default=text('0'))
    employment = db.Column(db.String(200), server_default='')
    create_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
    update_time = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return '%s' % self.username

    def check_password(self, password):
        return self.password == password


'''
    提供给登录模块使用，通用用户 id 获取用户
'''


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


'''
    向 ORM 提供 Post 数据映射对象及 Post 表结构
'''


class Post(db.Model):
    __tablename__ = 'Posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), server_default='')
    content = db.Column(db.Text, server_default='')
    author_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
    update_time = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    __mapper_args__ = {"order_by": create_time.desc()}

    def __repr__(self):
        return '%d' % self.id
