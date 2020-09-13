from app.main import bp
from app.models import Post
from flask import jsonify, request, render_template


@bp.route('/')
def index():
    return render_template('index.html')


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
    return jsonify({'data': data})
