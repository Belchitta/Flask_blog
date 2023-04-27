from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from blog.extensions import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(300), unique=True, nullable=False)
    text = db.Column(db.Text, default='Empty')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')
