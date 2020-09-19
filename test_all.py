import os

import pytest

from app import create_app

app = create_app()


# TODO: tests

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def login(client, username, password):
    return client.post('/auth/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def register(client, username, password, name='', gender=0, college='', major='', status='', employment=''):
    return client.post('/auth/register', data=dict(
        username=username,
        password=password,
        name=name,
        gender=gender,
        college=college,
        major=major,
        status=status,
        employment=employment
    ), follow_redirects=True)


def logout(client):
    return client.get('/auth/logout', follow_redirects=True)


def test_logout_without_login(client):
    r = logout(client)
    assert r.status_code == 401


def test_login_logout(client):
    r = login(client, 'admin', 'admin')
    j = r.get_json()
    assert j['success'] is True

    r = logout(client)
    j = r.get_json()
    assert j['success'] is True


def test_register(client):
    username = os.urandom(16)
    password = os.urandom(16)
    r = register(client, username, password)
    j = r.get_json()
    assert j['success'] is True

    r = login(client, username, password)
    j = r.get_json()
    assert j['success'] is True

    r = logout(client)
    j = r.get_json()
    assert j['success'] is True
