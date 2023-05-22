from flask_wtf import FlaskForm
from wtforms import (
    SubmitField, EmailField, PasswordField
)
from wtforms.validators import (
    DataRequired
)
class LoginForm(FlaskForm):
    mail = EmailField(
        "Электронная почта",
        validators=[DataRequired('Введите электронную почту')]
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired('Введите пароль')]
    )
    submit = SubmitField('Войти')