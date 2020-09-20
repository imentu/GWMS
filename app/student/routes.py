import json

from flask import jsonify, request
from flask_login import login_required, current_user

from app import db
from app.models import User
from app.student import bp


@bp.route('/')
def index():
    return 'Hello World!'


@bp.route('/status', methods=['GET'])
@login_required
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
    })


@bp.route('/status', methods=['POST'])
@login_required
def update_status():
    user = User.query.get(current_user.id)
    data = json.loads(request.get_data(as_text=True))
    user.status = data['status']
    user.employment = data['employment']
    if user.status is 0:
        user.employment = ''
    db.session.commit()
    return jsonify({'success': True, 'message': '更改就业状态成功'})
