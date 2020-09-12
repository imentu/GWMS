from app.auth import bp
from flask_login import login_user, logout_user
from app import db
from flask import request, jsonify
from app.auth.util import login_verify, register_verify


@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    verify_result = login_verify(username, password)
    if verify_result['user']:
        login_user(verify_result['user'])
    return jsonify(verify_result['info'])


@bp.route('/logout')
def logout():
    logout_user()
    return jsonify({'success': True, 'message': 'logout success'})


@bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    verify_result = register_verify(username, password)
    if verify_result['user']:
        db.session.add(verify_result['user'])
        db.session.commit()
    return jsonify(verify_result['info'])
