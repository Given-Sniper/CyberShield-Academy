from app.extensions import db


class QuizQuestion(db.Model):
    __tablename__ = 'quiz_questions'

    id = db.Column(db.BigInteger, primary_key=True)
    quiz_id = db.Column(db.BigInteger, db.ForeignKey('quizzes.id', ondelete='CASCADE'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    order_index = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    quiz = db.relationship('Quiz', back_populates='questions')

    def is_correct(self, submitted_option):
        return (submitted_option or '').upper() == self.correct_option.upper()

    def __repr__(self):
        return f'<QuizQuestion {self.id}>'
