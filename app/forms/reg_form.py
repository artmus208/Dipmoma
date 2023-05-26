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
    second_name = StringField(
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
    qual = SelectField(
        "Ваша квалификация",
        choices=[(-1, "Квалификация:")],
        default='Не указано',
        validators=[DataRequired("Укажите квалификацию")]
    )
    def validate_qual(form, field):
        if int(field.data) == -1:
            raise ValidationError(
                "Укажите квалификацию"
            )
    # Специалист по идентификации, студент, инженер, преподаватель
    other = StringField("Другое...", default='')
    submit = SubmitField("Регистрация")
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        quals = kwargs.get("quals", [])
        b = quals+[(len(quals)-1, "Другое...")]
        self.qual.choices+=b
        