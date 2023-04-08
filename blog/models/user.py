from flask_login import UserMixin
from blog.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(255), nullable=False, default="", server_default="")
    # password = db.Column(db.String(255))

    def __init__(self, email, username, is_staff):
        self.email = email
        self.username = username
        self.is_staff = is_staff
        # self.password = password
