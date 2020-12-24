from flask import request, jsonify
from flask_login import login_user, logout_user, login_required

from app import db
from app.auth import bp
from app.auth.util import login_verify, register_verify

'''
    用户登录接口
'''


@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']  # 从 POST 请求中获取用户名和密码
    verify_result = login_verify(username, password)  # 校验用户名密码
    if verify_result['user']:
        user = verify_result['user']
        login_user(user)  # 在服务器中保存用户登录状态
        verify_result['info']['user'] = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'type': user.type
        }  # 给登陆结果中添加需要在前端中展示的用户信息 id，用户名，姓名，用户类型
    return jsonify(verify_result['info'])  # 向前端返回登录结果


'''
    用户退出登录接口
'''


@bp.route('/logout')
@login_required
def logout():
    logout_user()  # 从服务器中删除当前用户登录状态
    return jsonify({'success': True, 'message': 'logout success'})


'''
    用户注册接口
'''


@bp.route('/register', methods=['POST'])
def register():
    # 从 POST 请求中获取表单中各项值
    # 用户名，密码，姓名，性别，学院，专业，就业状态，就业单位
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    gender = request.form['gender']
    college = request.form['college']
    major = request.form['major']
    status = request.form['status']
    employment = request.form['employment']
    verify_result = register_verify(username, password, name=name, gender=gender, college=college, major=major,
                                    status=status, employment=employment)  # 校验注册信息的合法性
    if verify_result['user']:
        db.session.add(verify_result['user'])  # 校验通过，向数据库添加新的用户对象
        db.session.commit()
    return jsonify(verify_result['info'])  # 向前端返回注册结果
