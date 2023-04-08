from flask_wtf import FlaskForm

from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField(
        "username",
        [validators.DataRequired()],
    )
    email = StringField(
        "Email Address",
        [
            validators.DataRequired(),
            validators.Email(),
            validators.Length(min=6, max=200),
        ],
        filters=[lambda data: data and data.lower()],
    )


class UserRegisterForm(FlaskForm):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    username = StringField('Username')
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Password again', [validators.DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField(
        "username",
        [validators.DataRequired()],
    )
    password = PasswordField(
        "Password",
        [validators.DataRequired()],
    )
    submit = SubmitField("Login")
