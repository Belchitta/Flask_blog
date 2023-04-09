from flask import Flask, render_template
from blog.models.user import User
from blog import commands
from blog.extensions import db, login_manager, migrate, csrf
from blog.views.auth import auth_app
from blog.views.authors import authors_app
from blog.views.users import users_app
from blog.views.articles import articles_app


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)

    login_manager.login_view = "auth_app.login"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).one_or_none()


def register_blueprints(app: Flask):
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")
    app.register_blueprint(authors_app, url_prefix='/authors')


def register_commands(app: Flask):
    # app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_articles)



