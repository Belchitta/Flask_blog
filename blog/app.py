import os

from flask import Flask

from blog.models import User
from blog.views.articles import articles_app
from blog.extensions import db, login_manager, migrate


def create_app() -> Flask:
    app = Flask(__name__)

    cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    login_manager.login_view = "auth_app.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).one_or_none()


def register_blueprints(app: Flask):
    from blog.views.auth import auth_app
    from blog.views.users import users_app

    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")


def register_commands(app: Flask):
    # app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_articles)


