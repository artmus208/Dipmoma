import os
import json
import plotly
import numpy as np
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.graph_objects as go


from . import logger
from flask import redirect, render_template, url_for, jsonify, flash, request, g, session
from .forms import UploadForm, IdentForm
from . import app
from . import data_collect
from .ident_methods import LSM

BASIDIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=["GET", "POST"])
def index():
    try:
        form = UploadForm()
        ident_form = IdentForm()
        ident_form.methods.choices=[(1, "МНК")]
        fig = go.Figure()
        file_path = None
        if form.validate_on_submit():
            filename = data_collect.save(form.file_upload.data)
            file_path = data_collect.path(filename)
            x, y = np.loadtxt(file_path, delimiter=',', unpack=True)
            fig.add_trace(go.Scatter(x=x, y=y, name="Исходная переходная характеристика объекта"))
            fig.update_layout(margin=dict(l=5, r=5, t=40, b=5),
                            title="Исходная переходная характеристика объекта",
                            xaxis_title="t, c",
                            yaxis_title="h(t)")
            dir_path = os.path.abspath(os.path.dirname(file_path))
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            dir_path += "\\test.JSON" # тут нужно имя пользователя .JSON или id объекта
            session["x"] = x.tolist()
            session["y"] = y.tolist()
            g.x = x.tolist()
            logger.debug(f"session['y'][0]: {session['y'][0]}")
            logger.debug(f"session['x'][0]: {session['x'][0]}")
            with open(dir_path, 'w') as file:
                file.write(f'var graphs = {graphJSON};')
            return render_template('index.html', ident_form=ident_form, form=form, file_url=file_path)
        return render_template('index.html', form=form, file_url=file_path)
    except Exception as e:
        logger.error(f"index: {e}")
        return redirect(url_for("index"))


@app.route('/system-ident', methods=['GET', 'POST'])
def system_ident():
    try:
        form = IdentForm(request.form)
        x, y = session.get("x", None), session.get("y", None)
        fig: go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, name="Исходная переходная характеристика объекта"))
        if x is None or y is None:
            logger.warning(f'/system-ident: x is None or y is None')
            return redirect(url_for('index'))
        # TODO:
        # [ ]: Надо добавить выбор степени идентификации
        # LSM(x, y, form.degree.data)
        fig.update_layout(
            title="Результат идентификации:"
        )
        fig.add_trace(go.Scatter())
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        logger.info(form.methods.data)
        return "Страница результата идентификации"
    except Exception as e:
        logger.error(f"/system-ident: {e}")
        return redirect(url_for("index"))



@app.route('/check-plotly', methods=['GET', 'POST'])
def check_plotly():
    x, y = np.loadtxt("time_value.txt", delimiter=',', unpack=True)
