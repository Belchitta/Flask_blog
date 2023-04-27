from flask_login import UserMixin
from sqlalchemy.orm import relationship

from blog.extensions import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(255), nullable=False, default="", server_default="")
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, email, username, is_staff, first_name, last_name, password):
        self.email = email
        self.username = username
        self.is_staff = is_staff
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
