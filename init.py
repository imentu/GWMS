import os
import time
import random
from common import basedir
from app import create_app, db
from app.models import User, Post

app = create_app()


def create_db():
    data_folder = os.path.join(basedir, 'data')
    if not os.path.exists(data_folder):
        print('data folder not exist, creating data folder.')
        os.mkdir(data_folder)
    db_path = os.path.join(data_folder, 'sys.db')
    if os.path.exists(db_path):
        print('sys.db already exist, deleting sys.db.')
        os.remove(db_path)
    db.create_all(app=app)
    print('db created.')


def rand_user():
    name_x = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何',
              '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
              '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆',
              '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
              '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚',
              '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪',
              '舒', '屈', '项', '祝', '董', '梁']
    name_m = ['玉', '明', '龙', '芳', '军', '玲', '', '立', '玲', '', '国', '一', '二', '三', '四', '五']
    alpha = 'abcdefghijklmnopqrstuvwxyzQBCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    colleges = ['计算机与信息工程学院', '机电工程学院', '经济管理学院']
    majors = ['物联网工程', '会计学', '机械制造']
    employments = ['黑煤窑', '传销公司', '保险公司']
    status = random.choice([0, 1])
    return User(username=''.join([random.choice(alpha) for i in range(8)]),
                password=''.join([random.choice(alpha) for i in range(8)]),
                name=random.choice(name_x) + random.choice(name_x) + random.choice(name_m),
                gender=random.choice([0, 1]),
                college=random.choice(colleges),
                major=random.choice(majors),
                status=status,
                employment=random.choice(employments) if status is 1 else '')


def add_test_data():
    with app.app_context():
        student = User(username='zz', password='123456', status=0)
        manager = User(username='admin', password='admin', type=2)

        db.session.add_all([rand_user() for i in range(500)])
        db.session.add(student)
        db.session.add(manager)
        db.session.commit()

        post = [Post(title=f'测试案例{i}', content='test', author_id=manager.id) for i in range(5)]

        db.session.add_all(post)
        db.session.commit()

    print('add test data succeed.')


if __name__ == '__main__':
    create_db()
    add_test_data()
