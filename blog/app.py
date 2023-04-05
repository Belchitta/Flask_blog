from flask import Flask

from blog.views.auth import auth_app, login_manager
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SECRET_KEY"] = "KrKwyKkTZNl2jJfCsgZYzcuiDPLamQ4C"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")
