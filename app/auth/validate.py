from app.models import User


def validate_username_password(username, password):
    result, message = True, 'login success'
    if not username or username.strip() is '':
        result, message = False, 'username error'
    if not password or password.strip() is '':
        result, message = False, 'password error'
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        result, message = False, 'username or password error'
        user = None
    return {'info': {'is_login': result, 'message': message}, 'user': user}
