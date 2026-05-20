from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db


class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    last_login_at = db.Column(db.DateTime, nullable=True)

    lessons = db.relationship('Lesson', back_populates='created_by_admin', lazy='dynamic')
    quizzes = db.relationship('Quiz', back_populates='created_by_admin', lazy='dynamic')
    phishing_examples = db.relationship('PhishingExample', back_populates='created_by_admin', lazy='dynamic')
    activities = db.relationship('Activity', back_populates='admin', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Admin {self.email}>'
