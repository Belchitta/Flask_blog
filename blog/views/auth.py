from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash, check_password_hash

from blog.extensions import login_manager, db
from blog.models.user import User
from blog.forms.user import UserRegisterForm, LoginForm

auth_app = Blueprint("auth_app", __name__)


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('index.html')


@auth_app.route("/login", methods=["GET", "POST"], endpoint="login")
def login():
    if current_user.is_authenticated:
        return render_template('index.html')

    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        password = request.form.get('password')
        if user is None:
            return render_template("auth/login.html", form=form, error="username doesn't exist")
        if not not check_password_hash(user.password, password):
            return render_template("auth/login.html", form=form, error="invalid username or password")

        login_user(user)
        return render_template('index.html')

    return render_template("auth/login.html", form=form)


@auth_app.route("/login-as/", methods=["GET", "POST"], endpoint="login-as")
def login_as():
    if not (current_user.is_authenticated and current_user.is_staff):
        # non-admin users should not know about this feature
        raise NotFound

    if request.method == "GET":
        return render_template("auth/login_as.html")

    username = request.form.get("username")
    if not username:
        return render_template("auth/login_as.html", error="username not passed")

    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/login_as.html", error=f"no user {username!r} found")

    login_user(user)
    return render_template('index.html')


@auth_app.route("/register/", methods=["GET", "POST"], endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append("username already exists!")
            return render_template("auth/register.html", form=form)

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template("auth/register.html", form=form)

        _user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            is_staff=False,
            password=generate_password_hash(form.password.data),
        )
        db.session.add(_user)
        db.session.commit()
        login_user(_user)

    return render_template('auth/register.html', form=form, errors=errors,)


@auth_app.route("/logout/")
@login_required
def logout():
    logout_user()
    return render_template('index.html')


@auth_app.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"


__all__ = [
    "login_manager",
    "auth_app",
]
