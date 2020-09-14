import os
import time
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


def add_test_data():
    with app.app_context():
        student1 = User(username='fuck', password='123456')
        student2 = User(username='zz', password='123456', status=1)
        manager = User(username='admin', password='admin', type=2)

        db.session.add(student1)
        db.session.add(student2)
        db.session.add(manager)
        db.session.commit()

        post = [Post(title=f'测试案例{i}', content='test', author_id=manager.id) for i in range(5)]

        db.session.add_all(post)
        db.session.commit()

    print('add test data succeed.')


if __name__ == '__main__':
    create_db()
    add_test_data()
