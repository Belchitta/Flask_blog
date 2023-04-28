from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from blog.extensions import db


article_tag_associations_table = Table(
    'article_tag_associations',
    db.metadata,
    db.Column('article_id', db.Integer, ForeignKey('article.id'), nullable=False),
    db.Column('tag_id', db.Integer, ForeignKey('tags.id'), nullable=False),
)


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    articles = relationship('Article', secondary=article_tag_associations_table, back_populates='tags')

    def __str__(self):
        return self.name
