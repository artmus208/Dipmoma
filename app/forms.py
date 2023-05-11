from wtforms import SubmitField, SelectField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from markupsafe import Markup
from . import data_collect

class UploadForm(FlaskForm):
    file_upload = FileField(
        validators=[FileRequired('Файл пустой!'),
                    FileAllowed(data_collect, "Только текстовый файл (.txt)")
        ],
    )
    submit = SubmitField('Загрузить')

class IdentForm(FlaskForm):
    methods = SelectField()
    submit = SubmitField('Запуск')