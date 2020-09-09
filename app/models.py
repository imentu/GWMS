from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Manager %r>' % self.username


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Offer %r>' % self.id
