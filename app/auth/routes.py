from flask import request, jsonify
from flask_login import login_user, logout_user, login_required

from app import db
from app.auth import bp
from app.auth.util import login_verify, register_verify


@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    verify_result = login_verify(username, password)
    if verify_result['user']:
        user = verify_result['user']
        login_user(user)
        verify_result['info']['user'] = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'type': user.type
        }
        return jsonify(verify_result['info'])


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'success': True, 'message': 'logout success'})


@bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    gender = request.form['gender']
    college = request.form['college']
    major = request.form['major']
    status = request.form['status']
    employment = request.form['employment']
    verify_result = register_verify(username, password, name=name, gender=gender, college=college, major=major,
                                    status=status, employment=employment)
    if verify_result['user']:
        db.session.add(verify_result['user'])
        db.session.commit()
    return jsonify(verify_result['info'])

