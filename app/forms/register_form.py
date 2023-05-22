from flask_wtf import FlaskForm
from wtforms import (
    SubmitField, SelectField, EmailField, PasswordField, StringField,
)
from wtforms.validators import (
    EqualTo, DataRequired, ValidationError
)


class RegisterForm(FlaskForm):
    first_name = StringField(
        "Ваше имя",
        validators=[DataRequired("Введите имя")]
    )
    
    second_name = SelectField(
        "Ваша фамилия",
        validators=[DataRequired("Введите фамилию")]
    )
    
    mail = EmailField(
        "Электронная почта",
        validators=[DataRequired("Введите почту")]
    )
    
    password = PasswordField(
        "Пароль", 
        validators=[
            EqualTo('confirm', 'Пароли должны совпасть'),
            DataRequired("Введите пароль")
        ],
    )
    
    confirm = PasswordField(
        'Повторите пароль',
        validators=[
            DataRequired("Подтвердите ввод пароля")
        ]
    )
    
    position = SelectField(
        "Чем вы занимаетесь?",    
    )
    def validate_position(form, field):
        if field.data == -1:
            raise ValidationError(
                "Выберите вид деятельности"
            )
    # Специалист по идентификации, студент, инженер, преподаватель
    other = StringField("Другое...", default='')
    submit = SubmitField("Регистрация")