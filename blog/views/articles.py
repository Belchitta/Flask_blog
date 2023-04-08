from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.views.users import USERS

articles_app = Blueprint("articles_app", __name__)

ARTICLES = {
    1: {
        'title': 'The extinction of polar ferrets is a global problem.',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque.'
                'Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis, '
                'porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae',
        'author': 2,
    },

    2: {
        'title': 'Will artificial intelligence replace clowns?',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque.'
                'Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis, '
                'porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae',
        'author': 3,
    },

    3: {
        'title': 'At the G20 summit, three old men fell on the slippery floor.',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque.'
                'Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis, '
                'porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae',
        'author': 1,
    },
}


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id: int):
    try:
        article_body = ARTICLES[article_id]
    except KeyError:
        raise NotFound(f"Article #{article_id} doesn't exist!")
    return render_template('articles/details.html', article_id=article_id, article_body=article_body, users=USERS)
