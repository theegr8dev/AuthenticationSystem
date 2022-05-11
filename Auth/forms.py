from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import EqualTo, Length, DataRequired, ValidationError, Email


class RegisterForm(FlaskForm):

    username = StringField(label="User Name", validators=[
                           Length(min=3), DataRequired()])

    email = EmailField(label="Email Address", validators=[
        Email(), DataRequired()])

    password = PasswordField(label="Password", validators=[
        DataRequired(), Length(min=5)])

    confirm_password = PasswordField(
        label="Confirm Password", validators=[EqualTo(password), DataRequired()])

    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="User Name", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    otp = StringField(label="OTP", validators=[DataRequired()])
    submit = SubmitField(label="Login In")
