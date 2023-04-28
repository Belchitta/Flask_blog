
from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.extensions import db
from blog.schemas import UserSchema
from blog.models.user import User


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }
