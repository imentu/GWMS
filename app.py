from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

'''
    毕业生工作管理系统 GWMS (Graduate Work Management System)
    管理员可以发布招聘信息， 毕业生需要填写当前找工作状态，教师可以实时查看，可以导出当前毕业生就业情况
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    return 'Hello World!'


# public api
@app.route('/offer')
def view_offer():
    pass


@app.route('/login')
def login():
    pass


@app.route('/logout')
def logout():
    pass


# manager api
@app.route('/manager/offer', methods=['POST'])
def publish_offer():
    pass


@app.route('/manager/students')
def check_students_status():
    pass


@app.route('/manager/students.xls')
def export_students_status():
    pass


# student api
@app.route('/student/status', methods=['POST'])
def update_status():
    pass


if __name__ == '__main__':
    app.run()
