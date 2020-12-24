import flask_excel as excel
from flask import jsonify
from flask import request
from flask_login import login_required, current_user

from app import db
from app.manager import bp
from app.manager.util import permission_required, students_records, students_records_for_export
from app.models import Post

'''
    获取所有学生信息的接口
'''


@bp.route('/students')
@login_required
@permission_required
def students():
    return jsonify({'data': students_records()})


'''
    导出接口，返回一个 excel 文件
'''


@bp.route('/export')
@login_required
@permission_required
def export():
    return excel.make_response_from_records(records=students_records_for_export(), file_type='xlsx')


'''
    创建新的招聘信息
'''


@bp.route('/post', methods=['POST'])
@login_required
@permission_required
def create_post():
    title = request.form['title']  # 从 POST 请求的表单中获取标题
    content = request.form['ckeditor']  # 从 POST 请求的表单中获取内容
    post = Post(title=title, content=content, author_id=current_user.id)
    db.session.add(post)  # 将招聘信息添加到数据库中
    db.session.commit()
    return jsonify({'success': True, 'message': 'create post success'})
