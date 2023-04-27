from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models.article import Article

articles_app = Blueprint("articles_app", __name__)

# ARTICLES = {
#     1: {
#         'title': 'The extinction of polar ferrets is a global problem.',
#         'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque.'
#                 'Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis, '
#                 'porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae',
#         'author': 2,
#     },
#
#     2: {
#         'title': 'Will artificial intelligence replace clowns?',
#         'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque.'
#                 'Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis, '
#                 'porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae',
#         'author': 3,
#     },
#
#     3: {
#         'title': 'At the G20 summit, three old men fell on the slippery floor.',
#         'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque.'
#                 'Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis, '
#                 'porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae',
#         'author': 1,
#     },
# }


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
