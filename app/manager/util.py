from collections import OrderedDict
from functools import wraps

from flask import current_app
from flask_login import current_user

from app.models import User

'''
    校验用户权限，根据当前用户的类型判断是否有权限访问接口
'''


def permission_required(func, level=1):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.type < level:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return decorated_view


'''
    从数据库中获取所有的学生对象
'''


def students_records():
    students_data = User.query.filter_by(type=0).all()
    data = [{
        'id': student.id,
        'name': student.name,
        'major': student.major,
        'college': student.college,
        'gender': '男' if student.gender is 0 else '女',
        'status': '待业' if student.status is 0 else '就业',
        'employment': student.employment,
    } for student in students_data]
    return data


'''
    从数据库中获取所有的学生对象，并将属性字段改为中文显示，用于导出时生成 excel 数据表
'''


def students_records_for_export():
    students_data = User.query.filter_by(type=0).all()
    data = [OrderedDict({
        '编号': student.id,
        '姓名': student.name,
        '性别': '男' if student.gender is 0 else '女',
        '学院': student.college,
        '专业': student.major,
        '就业状态': '待业' if student.status is 0 else '就业',
        '就业单位': student.employment,
    }) for student in students_data]
    return data
