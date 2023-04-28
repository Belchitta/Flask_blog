from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.extensions import db
from blog.schemas import ArticleSchema
from blog.models.article import Article


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }
