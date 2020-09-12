from flask import jsonify
from app.manager import bp
from app.models import User
from flask_login import login_required, current_user


@bp.route('/students')
@login_required
def students():
    students_data = User.query.filter_by(type=0).all()
    data = [{
        'id': student.id,
        'username': student.username,
        'password': student.password,
        'name': student.name,
        'major': student.major,
        'college': student.college,
        'gender': student.gender,
        'status': student.status,
        'employment': student.employment,
        'type': student.type
    } for student in students_data]
    return jsonify({'success': True, 'data': data})


@bp.route('/status.xlsx')
@login_required
def export_status():
    pass
