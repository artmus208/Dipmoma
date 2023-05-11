from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from . import data_collect

class UploadForm(FlaskForm):
    data = FileField('Файл с данными переходной характеристики',
                    validators=[FileRequired('Файл пустой!'),
                                FileAllowed(data_collect, "Только текстовый файл (.txt)")])
    submit = SubmitField('Загрузить')