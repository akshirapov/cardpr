from app import db
from datetime import datetime


class Hook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.String(200), default='')
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Hook ({self.id})>'
