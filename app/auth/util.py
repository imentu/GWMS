from app.models import User
from app import db


def validate_username_password(username, password, default_result, default_message):
    result, message = default_result, default_message
    if not username or username.strip() is '':
        result, message = False, 'username error.'
    if not password or password.strip() is '':
        result, message = False, 'password error.'
    return result, message


def login_verify(username, password):
    result, message = validate_username_password(username, password, True, 'login success')
    user = None
    if result:
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            result, message = False, 'username or password error.'
            user = None
    return {'info': {'success': result, 'message': message}, 'user': user}


def register_verify(username, password):
    result, message = validate_username_password(username, password, True, 'register success')
    user = None
    if result:
        user = User.query.filter_by(username=username).first()
        if user:
            result, message = False, 'username already exists.'
            user = None
        else:
            user = User(username=username, password=password)
    return {'info': {'success': result, 'message': message}, 'user': user}
