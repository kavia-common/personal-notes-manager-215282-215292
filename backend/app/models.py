from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance, initialized in app factory
db = SQLAlchemy()


class Note(db.Model):
    """SQLAlchemy model for Note."""
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, default="")
    content = db.Column(db.Text, nullable=False, default="")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Serialize model to dict with ISO8601 timestamps."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat() + "Z" if self.created_at else None,
            "updated_at": self.updated_at.isoformat() + "Z" if self.updated_at else None,
        }
