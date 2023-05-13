from wtforms import SubmitField, SelectField, IntegerField
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
