from app.auth import bp
from flask_login import login_user, logout_user
from app.models import User
from flask import request, jsonify
from app.auth.validate import validate_username_password


@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    validate_result = validate_username_password(username, password)
    if validate_result['user']:
        login_user(validate_result['user'])
    return jsonify(validate_result['info'])
