from flask import current_app
from functools import wraps
from flask_login import current_user


def permission_required(func, level=1):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.type < level:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return decorated_view
