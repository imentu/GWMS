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


def logout(client):
    return client.get('/auth/logout', follow_redirects=True)


def test_login_logout(client):
    rv = login(client, 'admin', 'admin')
    assert b'"success": true' in rv.data
