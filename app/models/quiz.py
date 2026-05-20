from app.extensions import db


class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(80), nullable=False)
    time_limit_seconds = db.Column(db.Integer, nullable=False)
    pass_mark_percent = db.Column(db.Integer, nullable=False, default=70)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_by_admin_id = db.Column(db.BigInteger, db.ForeignKey('admins.id', ondelete='SET NULL'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    created_by_admin = db.relationship('Admin', back_populates='quizzes')
    questions = db.relationship('QuizQuestion', back_populates='quiz', lazy='dynamic', cascade='all, delete-orphan')
    results = db.relationship('QuizResult', back_populates='quiz', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Quiz {self.title}>'
