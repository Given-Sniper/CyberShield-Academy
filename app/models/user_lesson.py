from app.extensions import db


class UserLesson(db.Model):
    __tablename__ = 'user_lessons'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    lesson_id = db.Column(db.BigInteger, db.ForeignKey('lessons.id', ondelete='CASCADE'), nullable=False)
    completed_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    user = db.relationship('User', back_populates='completed_lessons')
    lesson = db.relationship('Lesson', back_populates='user_lessons')

    __table_args__ = (db.UniqueConstraint('user_id', 'lesson_id', name='uq_user_lessons_unique_completion'),)

    def __repr__(self):
        return f'<UserLesson user={self.user_id} lesson={self.lesson_id}>'
