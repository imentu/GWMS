from flask import jsonify
from app.manager import bp
from flask_login import login_required
from app.manager.util import permission_required, students_records, students_records_for_export
import flask_excel as excel


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
