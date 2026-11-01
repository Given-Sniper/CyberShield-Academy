import pytest
from flask import g
from sqlalchemy import select
from app.models import Admin, User

PASSWORD = 'a long test password'


def test_registration_login_logout(client, db):
    response = client.post('/auth/register', data={
        'email': 'Learner@example.com', 'full_name': 'Learner',
        'password': PASSWORD, 'confirm_password': PASSWORD,
    })
    assert response.status_code == 302
    user = db.session.scalar(select(User))
    assert user.email == 'learner@example.com'
    assert user.password_hash != PASSWORD
    assert user.check_password(PASSWORD)
    assert client.post('/auth/login', data={'email': user.email, 'password': 'wrong'}).status_code == 200
    assert client.get('/dashboard/').status_code == 302
    response = client.post('/auth/login?next=https://example.com', data={'email': user.email, 'password': PASSWORD})
    assert response.location.endswith('/dashboard/')
    assert client.get('/dashboard/').status_code == 200
    assert client.get('/admin/').status_code == 302
    assert client.get('/auth/logout').status_code == 405
    assert client.post('/auth/logout').status_code == 302
    assert client.get('/dashboard/').status_code == 302


def test_registration_validation_and_duplicates(client, db):
    data = {'email': 'user@example.com', 'full_name': 'User', 'password': PASSWORD, 'confirm_password': PASSWORD}
    client.post('/auth/register', data=data)
    data['email'] = 'USER@example.com'
    assert b'already exists' in client.post('/auth/register', data=data).data
    data['email'] = 'new@example.com'
    data['password'] = data['confirm_password'] = 'short'
    assert client.post('/auth/register', data=data).status_code == 200
    assert len(db.session.scalars(select(User)).all()) == 1


def test_admin_login_and_deactivation(client, db):
    admin = Admin(email='admin@example.com')
    admin.set_password(PASSWORD)
    db.session.add(admin)
    db.session.commit()
    assert client.post('/auth/admin/login', data={'email': admin.email, 'password': PASSWORD}).status_code == 302
    assert client.get('/admin/').status_code == 200
    assert client.get('/dashboard/').status_code == 302
    admin.is_active = False
    db.session.commit()
    db.session.remove()
    # The db fixture holds an application context; clear its cached principal
    # to model the fresh application context of a real subsequent request.
    g.pop('_login_user', None)
    assert client.get('/admin/').status_code == 302
    client.post('/auth/admin/logout')
    assert client.post('/auth/admin/login', data={'email': 'admin@example.com', 'password': PASSWORD}).status_code == 200
    assert client.get('/admin/').status_code == 302
    assert client.post('/auth/admin/register').status_code == 403


@pytest.mark.parametrize('path', ['/admin/', '/admin/users', '/dashboard/', '/lessons/', '/quizzes/', '/phishing/'])
def test_anonymous_routes_are_protected(client, path):
    assert client.get(path).status_code == 302


def test_csrf_rejects_missing_token(app, client):
    app.config['WTF_CSRF_ENABLED'] = True
    assert client.post('/auth/login', data={'email': 'test@example.com', 'password': PASSWORD}).status_code == 400
    assert client.post('/auth/logout').status_code == 400


def test_create_admin_command(app, db):
    result = app.test_cli_runner().invoke(args=['create-admin', '--email', 'admin@example.com'], input=f'{PASSWORD}\n{PASSWORD}\n')
    assert result.exit_code == 0
    admin = db.session.scalar(select(Admin))
    assert admin.check_password(PASSWORD)
