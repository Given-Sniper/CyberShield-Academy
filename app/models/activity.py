from app.extensions import db


class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    admin_id = db.Column(db.BigInteger, db.ForeignKey('admins.id', ondelete='SET NULL'), nullable=True)
    activity_type = db.Column(db.String(80), nullable=False)
    activity_details = db.Column(db.JSON, nullable=True)
    reference_type = db.Column(db.String(80), nullable=True)
    reference_id = db.Column(db.BigInteger, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    user = db.relationship('User', back_populates='activities')
    admin = db.relationship('Admin', back_populates='activities')

    def __repr__(self):
        return f'<Activity {self.activity_type}>'
