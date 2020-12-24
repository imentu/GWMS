from app.models import User

'''
    用于校验用户名和密码是否为空
'''


def validate_username_password(username, password, default_result, default_message):
    result, message = default_result, default_message
    if not username or username.strip() is '':
        result, message = False, '用户名不能为空'
    if not password or password.strip() is '':
        result, message = False, '密码不能为空'
    return result, message


'''
    用于登录时校验用户名和密码的正确性
'''


def login_verify(username, password):
    result, message = validate_username_password(username, password, True, '登录成功')  # 校验用户名和密码是否为空
    user = None
    if result:
        user = User.query.filter_by(username=username).first()  # 根据用户名查询用户对象
        if not user or not user.check_password(password):  # 如果对应的用户不存在或密码不一致，登录失败
            result, message = False, '用户名或密码错误'
            user = None
    return {'info': {'success': result, 'message': message}, 'user': user}


'''
    用于注册时校验各字段的合法性
'''


def register_verify(username, password, name='', gender=0, college='', major='', status='', employment=''):
    result, message = validate_username_password(username, password, True, '注册成功')  # 校验用户名和密码是否为空
    user = None
    if result:
        user = User.query.filter_by(username=username).first()  # 用username去数据库查询用户
        if user:  # 如果查到用户，说明用户名重复，不可注册
            result, message = False, '该用户名已存在'
            user = None
        else:
            user = User(username=username, password=password, name=name, gender=gender, college=college, major=major,
                        status=status, employment=employment)  # 构建user对象准备添加到数据库
    return {'info': {'success': result, 'message': message}, 'user': user}
