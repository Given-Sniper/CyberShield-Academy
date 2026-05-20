from app.extensions import db


class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    difficulty_level = db.Column(db.String(30), nullable=False)
    created_by_admin_id = db.Column(db.BigInteger, db.ForeignKey('admins.id', ondelete='SET NULL'), nullable=True)
    is_published = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    created_by_admin = db.relationship('Admin', back_populates='lessons')
    user_lessons = db.relationship('UserLesson', back_populates='lesson', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Lesson {self.title}>'
