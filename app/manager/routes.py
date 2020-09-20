import flask_excel as excel
from flask import jsonify
from flask import request
from flask_login import login_required, current_user

from app import db
from app.manager import bp
from app.manager.util import permission_required, students_records, students_records_for_export
from app.models import Post


# TODO: integration ckeditor

@bp.route('/students')
@login_required
@permission_required
def students():
    return jsonify({'data': students_records()})


@bp.route('/export')
@login_required
@permission_required
def export():
    return excel.make_response_from_records(records=students_records_for_export(), file_type='xlsx')


@bp.route('/post', methods=['POST'])
@login_required
@permission_required
def create_post():
    title = request.form['title']
    content = request.form['ckeditor']
    post = Post(title=title, content=content, author_id=current_user.id)
    db.session.add(post)
    db.session.commit()
    return ''
