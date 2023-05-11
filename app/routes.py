import os
import json
import plotly
import numpy as np
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.graph_objects as go


from . import logger
from flask import redirect, render_template, url_for, jsonify, flash, request, g
from .forms import UploadForm, IdentForm
from . import app
from . import data_collect
from .ident_methods import LSM

BASIDIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=["GET", "POST"])
def index():
    form = UploadForm()
    ident_form = IdentForm()
    ident_form.methods.choices=[(1, "МНК")]
    fig = go.Figure()

    file_path = None
    if form.validate_on_submit():
        filename = data_collect.save(form.file_upload.data)
        file_path = data_collect.path(filename)
        logger.info(file_path)
        x, y = np.loadtxt(file_path, delimiter=',', unpack=True)
        fig.add_trace(go.Scatter(x=x, y=y, name="Исходная переходная характеристика объекта"))
        fig.update_layout(margin=dict(l=5, r=5, t=40, b=5),
                          title="Исходная переходная характеристика объекта",
                          xaxis_title="t, c",
                          yaxis_title="h(t)")
        g.fig = fig
        g.x = x
        g.y = y
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        dir_path = os.path.abspath(os.path.dirname(file_path))
        logger.info(dir_path)
        dir_path += "\\test.JSON"
        with open(dir_path, 'w') as file:
            file.write(f'var graphs = {graphJSON};')
        return render_template('index.html', ident_form=ident_form, form=form, file_url=file_path)
    return render_template('index.html', form=form, file_url=file_path)


@app.route('/system-ident', methods=['GET', 'POST'])
def system_ident():
    form = IdentForm(request.form)
    fig: go.Figure = getattr(g, 'fig', None)
    x = getattr(g, 'x', None)
    y = getattr(g, 'y', None)
    if fig is None or x is None or y is None:
        logger.warning(f'/system-ident: fig is None or x is None or y is None')
        return redirect(url_for('index'))
    # TODO:
    # [ ]: Надо добавить выбор степени идентификации

    LSM(x, y, 2)

    fig.update_layout(
        title="Результат идентификации:"
    )
    fig.add_trace(go.Scatter())
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    logger.info(form.methods.data)
    return "Страница результата идентификации"



@app.route('/check-plotly', methods=['GET', 'POST'])
def check_plotly():
    x, y = np.loadtxt("time_value.txt", delimiter=',', unpack=True)
