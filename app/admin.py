from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

'''
    后台管理页面的配置类
'''


class UserView(ModelView):
    permission_level = 2

    def is_accessible(self):
        return current_user.is_authenticated and current_user.type >= self.permission_level  # 校验用户权限

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.index'))  # 如果用户权限不足，跳转到首页

    page_size = 50  # 设置单页显示数据条数
    column_searchable_list = ['name', 'username']  # 设置可搜索项
    column_filters = ['gender', 'college', 'type', 'major', 'employment']  # 设置可过滤列
    form_choices = {  # 限定更新用户时的表单可选项
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
        return current_user.is_authenticated and current_user.type >= self.permission_level  # 校验用户访问权限

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.index'))  # 权限不足时跳转

    page_size = 50  # 单页最大数据条数
    column_searchable_list = ['title', 'content']  # 可搜索的列
    column_filters = ['author']  # 设置可过滤列
    create_modal = False  # 不可在后台中创建新的招聘信息
    form_ajax_refs = {  # 通过外键找到用户的跳转地址
        'author': {
            'fields': ['id', 'username'],
            'page_size': 10
        }
    }
