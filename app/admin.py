from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class UserView(ModelView):
    permission_level = 2

    def is_accessible(self):
        return current_user.is_authenticated and current_user.type >= self.permission_level

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.index'))

    page_size = 50
    column_searchable_list = ['name', 'username']
    column_filters = ['gender', 'college', 'type', 'major', 'employment']
    form_choices = {
        'gender': [
            ('0', '男'),
            ('1', '女')
        ],
        'type': [
            ('0', '学生'),
            ('1', '管理员'),
            ('2', '超级管理员')
        ],
        'status': [
            ('0', '待业'),
            ('1', '就业')
        ]
    }


class PostView(ModelView):
    permission_level = 2

    def is_accessible(self):
        return current_user.is_authenticated and current_user.type >= self.permission_level

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.index'))

    page_size = 50
    column_searchable_list = ['title', 'content']
    column_filters = ['author']
    create_modal = False
    form_ajax_refs = {
        'author': {
            'fields': ['id', 'username'],
            'page_size': 10
        }
    }
