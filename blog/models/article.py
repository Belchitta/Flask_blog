from sqlalchemy import Column, Integer, String, Text, DateTime, func
from blog.extensions import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(300), unique=True, nullable=False)
    text = Column(Text, default='Empty')
    date = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"Article #{self.id} {self.title!r} {self.date!r}>"
