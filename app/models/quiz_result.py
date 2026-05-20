from app.extensions import db


class QuizResult(db.Model):
    __tablename__ = 'quiz_results'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    quiz_id = db.Column(db.BigInteger, db.ForeignKey('quizzes.id', ondelete='CASCADE'), nullable=False)
    score_percent = db.Column(db.Numeric(5, 2), nullable=False)
    correct_answers = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    passed = db.Column(db.Boolean, nullable=False)
    started_at = db.Column(db.DateTime, nullable=False)
    submitted_at = db.Column(db.DateTime, nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='quiz_results')
    quiz = db.relationship('Quiz', back_populates='results')

    def __repr__(self):
        return f'<QuizResult user={self.user_id} quiz={self.quiz_id}>'
