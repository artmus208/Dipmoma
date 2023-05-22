from wtforms import (
    SubmitField, SelectField, IntegerField,
    EmailField, PasswordField, StringField,
)
from wtforms.validators import (
    EqualTo, DataRequired, ValidationError
)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from markupsafe import Markup
from . import data_collect

class UploadForm(FlaskForm):
    
    file_upload = FileField(
        validators=[FileRequired('Файл пустой!'),
                    FileAllowed(data_collect, "Только текстовый файл (.txt)")
        ],
        render_kw={
            "accesskey": "f"
        }
    )
    submit = SubmitField('Загрузить',
        render_kw={
            "accesskey": "d"
        })

class IdentForm(FlaskForm):
    methods = SelectField()
    degree = IntegerField(render_kw={
        "min": 1,
        "placeholder":u"Степень полинома знаменателя",
        "size": 100,
        })
    submit = SubmitField('Запуск')

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