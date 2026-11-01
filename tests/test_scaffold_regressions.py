from datetime import datetime

import pytest
from flask_login import current_user
from flask_migrate import downgrade, upgrade
from sqlalchemy import inspect

from app.models import (Activity, Admin, Lesson, PhishingExample, Quiz,
                        QuizQuestion, QuizResult, User, UserLesson)
from app.utils.decorators import admin_required, login_required_user


def test_all_models_generate_ids(db):
    user = User(email='user@example.com', password_hash='hash')
    admin = Admin(email='admin@example.com', password_hash='hash')
    lesson = Lesson(title='Lesson', content='Content', category='Phishing Attacks',
                    difficulty_level='Beginner', created_by_admin=admin)
    quiz = Quiz(title='Quiz', category='Phishing Attacks', time_limit_seconds=60,
                created_by_admin=admin)
    question = QuizQuestion(quiz=quiz, question_text='Question?', option_a='A',
                            option_b='B', option_c='C', option_d='D', correct_option='A')
    result = QuizResult(user=user, quiz=quiz, score_percent=100, correct_answers=1,
                        total_questions=1, passed=True, started_at=datetime.now(),
                        submitted_at=datetime.now(), duration_seconds=1)
    completion = UserLesson(user=user, lesson=lesson)
    activity = Activity(user=user, activity_type='user_login')
    phishing = PhishingExample(example_type='email', title='Example', content='Text')
    rows = [user, admin, lesson, quiz, question, result, completion, activity, phishing]
    db.session.add_all(rows)
    db.session.commit()
    assert all(row.id is not None for row in rows)
    assert result.user_id == user.id
    assert completion.lesson_id == lesson.id


@pytest.mark.parametrize('scope', ['user', 'admin'])
def test_session_restores_correct_role_with_overlapping_ids(app, db, client, scope):
    user = User(email='user@example.com', password_hash='hash')
    admin = Admin(email='admin@example.com', password_hash='hash')
    db.session.add_all([user, admin])
    db.session.commit()
    assert user.id == admin.id

    @app.route('/_test/user')
    @login_required_user
    def user_only():
        return current_user.get_id()

    @app.route('/_test/admin')
    @admin_required
    def admin_only():
        return current_user.get_id()

    identity = (user if scope == 'user' else admin).get_id()
    with client.session_transaction() as session:
        session['_user_id'] = identity
        session['_fresh'] = True
    db.session.remove()
    response = client.get(f'/_test/{scope}')
    assert response.status_code == 200
    assert response.text == identity
    other = 'admin' if scope == 'user' else 'user'
    denied = client.get(f'/_test/{other}')
    assert denied.status_code == 302
    assert denied.location.endswith('/auth/admin/login' if other == 'admin' else '/auth/login')


def test_migration_upgrade_and_downgrade(app):
    from app.extensions import db
    with app.app_context():
        upgrade()
        assert set(db.metadata.tables).issubset(inspect(db.engine).get_table_names())
        user = User(email='migrated@example.com', password_hash='hash')
        db.session.add(user)
        db.session.commit()
        assert user.id is not None
        db.session.remove()
        downgrade(revision='base')
        assert not set(db.metadata.tables).intersection(inspect(db.engine).get_table_names())
