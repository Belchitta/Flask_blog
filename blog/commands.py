import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


# @click.command("init-db")
# def init_db():
#     db.create_all()
#     print("Done!")


@click.command('create-init-user')
def create_init_user():
    from blog.models.user import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='name@example.com', password=generate_password_hash('test123'))
        )
        db.session.commit()


@click.command("create-users")
def create_users():
    from blog.models.user import User
    from wsgi import app
    with app.app_context():
        super = User(email='admin@mail.com', username="admin_", is_staff=True)
        samuel = User(email='samu@mail.com', username="samuel", is_staff=False)

        db.session.add(super)
        db.session.add(samuel)
        db.session.commit()

        click.echo('Created users!')


@click.command("create-articles")
def create_articles():
    from blog.models.article import Article
    from wsgi import app
    with app.app_context():
        first = Article(
            title="The extinction of polar ferrets is a global problem.",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque."
                 "Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis,"
                 "porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae"
        )
        second = Article(
            title="Will artificial intelligence replace clowns?",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque."
                 "Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis, "
                 "porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae"
        )
        third = Article(
            title="At the G20 summit, three old men fell on the slippery floor.",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eu dapibus leo. Proin non sem neque."
                 "Donec nec accumsan ante. Proin venenatis nisl quis sapien aliquam malesuada. Maecenas turpis felis, "
                 "porttitor eget pellentesque a, viverra id turpis. Quisque a magna eu nulla sodales maximus vitae"
        )

        db.session.add(first)
        db.session.add(second)
        db.session.add(third)
        db.session.commit()

        click.echo('Created articles!')


@click.command('create-init-tags')
def create_init_tags():
    from blog.models.tag import Tag
    from wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')
