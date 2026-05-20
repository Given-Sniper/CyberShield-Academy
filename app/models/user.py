from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=True)
    security_question = db.Column(db.String(255), nullable=True)
    security_answer_hash = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    last_login_at = db.Column(db.DateTime, nullable=True)

    quiz_results = db.relationship('QuizResult', back_populates='user', lazy='dynamic', cascade='all, delete-orphan')
    activities = db.relationship('Activity', back_populates='user', lazy='dynamic', cascade='all, delete-orphan')
    completed_lessons = db.relationship('UserLesson', back_populates='user', lazy='dynamic', cascade='all, delete-orphan')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return f'user:{self.id}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_security_answer(self, answer):
        self.security_answer_hash = generate_password_hash(answer)

    def check_security_answer(self, answer):
        if not self.security_answer_hash:
            return False
        return check_password_hash(self.security_answer_hash, answer)

    def __repr__(self):
        return f'<User {self.email}>'
