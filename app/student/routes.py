import json
from app import db
from app.student import bp
from app.models import User, Post
from flask import jsonify, request
from flask_login import login_required, current_user


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
    user.name = data['name']
    user.major = data['major']
    user.college = data['college']
    user.gender = data['gender']
    user.status = data['status']
    user.employment = data['employment']
    db.session.commit()
    return jsonify({'success': True, 'message': 'update status success.'})
