import getopt
import os
import random
import string
import sys

from app import create_app, db
from app.models import User, Post

app = create_app()
basedir = os.path.abspath(os.path.dirname(__file__))


def rand_user():
    name_x = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何',
              '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
              '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆',
              '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
              '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚',
              '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪',
              '舒', '屈', '项', '祝', '董', '梁']
    name_m = ['玉', '明', '龙', '芳', '军', '玲', '', '立', '玲', '', '国', '一', '二', '三', '四', '五']
    colleges = ['计算机与信息工程学院', '机电工程学院', '经济管理学院']
    majors = ['物联网工程', '会计学', '机械制造']
    employments = ['黑煤窑', '传销公司', '保险公司']
    status = random.choice([0, 1])
    return User(username=''.join(random.sample(string.ascii_letters + string.digits, 8)),
                password=''.join(random.sample(string.ascii_letters + string.digits, 8)),
                name=random.choice(name_x) + random.choice(name_x) + random.choice(name_m),
                gender=random.choice([0, 1]),
                college=random.choice(colleges),
                major=random.choice(majors),
                status=status,
                employment=random.choice(employments) if status is 1 else '')


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

    with app.app_context():
        manager = User(username='admin', password='admin', type=2)
        db.session.add(manager)
        db.session.commit()


def add_test_data():
    with app.app_context():
        student = User(username='zz', password='123456', status=0)

        db.session.add_all([rand_user() for i in range(30)])
        db.session.add(student)
        db.session.commit()

        admin = User.query.filter_by(username='admin').first()

        post = [Post(title=f'python讲师-{i}',
                     content='<p><strong>职位描述：</strong></p><ul><li>【岗位职责】<ul><li>Python课程讲师，0基础课程，远程授课，受众为美国留学生</li><li>设计课程、课上授课、课后答疑</li><li>每节课2小时，每周4节课，每个课题2周</li><li>首次开课时间：10月20日左右</li></ul></li><li>【任职要求】<ul><li>可以使用英语为授课语言</li><li>美国US News综合排名Top 40学校 or CS专业排名TOP 15学校 or QS世界大学排名TOP 60学校 or&nbsp;国内外大厂正式员工（BAT、美团、字节、谷歌、亚马逊等）</li><li>CS相关专业，可以熟练使用Python，研究生或者博士生在读</li></ul></li><li>【薪资待遇】<ul><li>450-500人民币每小时，条件优秀者薪资可面议。每课题2周共计16小时</li><li>提供实习证明，优秀导师可获得企业推荐信，获得更多工作机会</li></ul></li></ul>',
                     author_id=admin.id) for i in range(3)]

        db.session.add_all(post)
        db.session.commit()

    print('add tests data succeed.')


if __name__ == '__main__':
    create_db()
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'd')
        if opts:
            add_test_data()
    except getopt.GetoptError:
        pass
