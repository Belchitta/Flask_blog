from flask import render_template
from blog.app import create_app
from blog.extensions import db

app = create_app()


@app.route('/', endpoint="index")
def start():
    return render_template("index.html")


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Done!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User
    admin = User(username="Admin", is_staff=True)
    sam = User(username="Sam")
    jane = User(username="Jane")
    john = User(username="John")

    db.session.add(admin)
    db.session.add(sam)
    db.session.add(jane)
    db.session.add(john)
    db.session.commit()

    print("Done! Created users:", admin, sam, jane, john)


@app.cli.command("create-articles")
def create_articles():
    from blog.models import Article
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

    print("Done! Articles created!")
