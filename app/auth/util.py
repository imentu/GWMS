from app.models import User


def validate_username_password(username, password, default_result, default_message):
    result, message = default_result, default_message
    if not username or username.strip() is '':
        result, message = False, '用户名不能为空'
    if not password or password.strip() is '':
        result, message = False, '密码不能为空'
    return result, message


def login_verify(username, password):
    result, message = validate_username_password(username, password, True, '登陆成功')
    user = None
    if result:
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            result, message = False, '用户名或密码错误'
            user = None
    return {'info': {'success': result, 'message': message}, 'user': user}


def register_verify(username, password, name='', gender=0, college='', major='', status='', employment=''):
    result, message = validate_username_password(username, password, True, '注册成功')
    user = None
    if result:
        user = User.query.filter_by(username=username).first()
        if user:
            result, message = False, '该用户名已存在'
            user = None
        else:
            user = User(username=username, password=password, name=name, gender=gender, college=college, major=major,
                        status=status, employment=employment)
    return {'info': {'success': result, 'message': message}, 'user': user}
