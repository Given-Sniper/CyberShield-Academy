from app.extensions import db


class PhishingExample(db.Model):
    __tablename__ = 'phishing_examples'

    id = db.Column(db.BigInteger, primary_key=True)
    example_type = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sender_display_name = db.Column(db.String(120), nullable=True)
    sender_email = db.Column(db.String(255), nullable=True)
    target_url = db.Column(db.String(500), nullable=True)
    has_urgent_language = db.Column(db.Boolean, nullable=False, default=False)
    has_suspicious_url = db.Column(db.Boolean, nullable=False, default=False)
    has_misspelling = db.Column(db.Boolean, nullable=False, default=False)
    difficulty_level = db.Column(db.String(30), nullable=False, default='Beginner')
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_by_admin_id = db.Column(db.BigInteger, db.ForeignKey('admins.id', ondelete='SET NULL'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    created_by_admin = db.relationship('Admin', back_populates='phishing_examples')

    def __repr__(self):
        return f'<PhishingExample {self.title}>'
