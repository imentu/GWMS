from flask import jsonify, render_template
from flask_login import current_user, login_required

from app.main import bp
from app.models import Post, User

'''
    服务器首页
'''


@bp.route('/')
def index():
    return render_template('index.html')


'''
    获取全部招聘信息
'''


@bp.route('/posts')
def posts():
    posts_data = Post.query.all()
    data = [{
        'id': post.id,
        'title': post.title,
        'author': post.author.name,
        'content': post.content,
        'update_time': post.update_time
    } for post in posts_data]
    return jsonify({'data': data})  # 向前端返回招聘信息列表


'''
    获取当前登录用户基本信息
'''


@bp.route('/user')
@login_required
def user_info():
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
        'name': current_user.name,
        'type': current_user.type,
    })


'''
    查询对应用户名是否存在
'''


@bp.route('/users/<username>/exists')
def is_username_exists(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'exists': True})
    else:
        return jsonify({'exists': False})
