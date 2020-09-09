from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, logout_user

'''
    毕业生工作管理系统 GWMS (Graduate Work Management System)
    管理员可以发布招聘信息， 毕业生需要填写当前找工作状态，教师可以实时查看，可以导出当前毕业生就业情况
'''

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/test.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
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
    info = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Offer %r>' % self.id


@app.route('/')
def hello_world():
    return 'Hello World!'


# public api
@app.route('/offers')
def view_offers():
    offers = Offer.query.all()
    res = [{'id': offer.id, 'info': offer.info} for offer in offers]
    return jsonify(res)


@app.route('/register', methods=['POST'])
def register():
    message = 'register success'
    username = request.form['username']
    password = request.form['password']
    if username and password:
        student = Student(username=username, password=password, status=0)
        db.session.add(student)
        db.session.commit()
    else:
        message = 'register failed'
    return message


@app.route('/login', methods=['POST'])
def login():
    pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'logout'


# manager api
@app.route('/manager/offer', methods=['POST'])
def publish_offer():
    pass


@app.route('/manager/students')
def check_students_status():
    students = Student.query.all()
    res = [{'id': student.id, 'username': student.username, 'status': student.status} for student in students]
    return jsonify(res)


@app.route('/manager/students.xls')
def export_students_status():
    pass


# student api
@app.route('/student/status', methods=['POST'])
def update_student_status():
    pass


if __name__ == '__main__':
    app.run()
