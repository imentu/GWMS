import json

from flask import jsonify, request
from flask_login import login_required, current_user

from app import db
from app.models import User
from app.student import bp


@bp.route('/')
def index():
    return 'Hello World!'


'''
    获取用户信息的接口
'''


@bp.route('/status', methods=['GET'])
@login_required  # 检测登录状态的过滤器，如果用户未登录，拒绝服务并提醒用户登录
def status():
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
        'name': current_user.name,
        'major': current_user.major,
        'college': current_user.college,
        'gender': current_user.gender,
        'status': current_user.status,
        'employment': current_user.employment
    })  # 把当前登录的用户对象转换为 json格式 返回到前端


'''
    更新学生就业状态的接口
'''


@bp.route('/status', methods=['POST'])
@login_required
def update_status():
    user = User.query.get(current_user.id)  # 根据当前登录用户的id获取数据库中当前用户对象
    data = json.loads(request.get_data(as_text=True))  # 解码请求中的 json 对象
    user.status = data['status']  # 获取新的用户就业状态 0 为待业 1 为就业
    user.employment = data['employment']  # 获取用户就业单位字段
    if user.status is 0:
        user.employment = ''  # 如果用户就业状态为待业，将就业单位修改为空
    db.session.commit()  # 向数据库提交修改
    return jsonify({'success': True, 'message': '更改就业状态成功'})  # 向前端返回结果
