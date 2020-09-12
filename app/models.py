from app import db
from flask_login import UserMixin
from sqlalchemy import text
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    type = db.Column(db.Integer, nullable=False, server_default=text('0'))
    status = db.Column(db.Integer, nullable=False, server_default=text('0'))
    create_time = db.Column(db.DateTime, nullable=False, server_default=func.now())

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def check_password(self, password):
        return self.password == password


class Post(db.Model):
    __tablename__ = 'Posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, server_default='')
    author_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
    update_time = db.Column(db.DateTime, nullable=False, server_default=func.now(), server_onupdate=func.now())

    def __repr__(self):
        return '<Post %r>' % self.id
