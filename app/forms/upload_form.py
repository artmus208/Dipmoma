from flask_wtf import FlaskForm
from wtforms import (
    SubmitField, SelectField, IntegerField,
    EmailField, PasswordField, StringField,
)
from wtforms.validators import (
    EqualTo, DataRequired, ValidationError
)
from flask_wtf.file import FileField, FileRequired, FileAllowed
from forms import data_collector


class UploadForm(FlaskForm):
    
    file_upload = FileField(
        validators=[FileRequired('Файл пустой!'),
                    FileAllowed(data_collector, "Только текстовый файл (.txt)")
        ],
        render_kw={
            "accesskey": "f"
        }
    )
    submit = SubmitField('Загрузить',
        render_kw={
            "accesskey": "d"
        })