from flask_wtf import FlaskForm
from wtforms import (
    SubmitField, SelectField, IntegerField,
)

class IdentForm(FlaskForm):
    methods = SelectField()
    degree = IntegerField(render_kw={
        "min": 1,
        "placeholder":u"Степень полинома знаменателя",
        "size": 100,
        })
    submit = SubmitField('Запуск')