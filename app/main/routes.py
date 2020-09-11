from app import db
from app.main import bp
from app.models import User, Post
from flask import jsonify, request
from flask_login import login_required, logout_user


@bp.route('/')
def hello_world():
    return 'Hello World!'


# # public api
# @bp.route('/offers')
# def view_offers():
#     offers = Offer.query.all()
#     res = [{'id': offer.id, 'info': offer.info} for offer in offers]
#     return jsonify(res)

#
# @bp.route('/register', methods=['POST'])
# def register():
#     message = 'register success'
#     username = request.form['username']
#     password = request.form['password']
#     if username and password:
#         student = Student(username=username, password=password, status=0)
#         db.session.add(student)
#         db.session.commit()
#     else:
#         message = 'register failed'
#     return message


@bp.route('/login', methods=['POST'])
def login():
    pass


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'logout'


# manager api
@bp.route('/manager/offer', methods=['POST'])
def publish_offer():
    pass


# @bp.route('/manager/students')
# def check_students_status():
#     students = Student.query.all()
#     res = [{'id': student.id, 'username': student.username, 'password': student.password,
#             'status': student.status} for student in students]
#     return jsonify(res)


@bp.route('/manager/students.xls')
def export_students_status():
    pass


# student api
@bp.route('/student/status', methods=['POST'])
def update_student_status():
    pass
