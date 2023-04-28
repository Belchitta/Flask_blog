from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models.article import Article
from blog.models.author import Author

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id: int):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if article is None:
        raise NotFound(f"User #{article_id} doesn't exist!")
    return render_template('articles/details.html', article=article)


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)
        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.commit()

        _article.author = current_user.author
        db.session.add(_article)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article_id=_article.id))
    return render_template("articles/create.html", form=form, error=error)
