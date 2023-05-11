import os
import json
import plotly
import numpy as np
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.graph_objects as go


from . import logger
from flask import redirect, render_template, url_for, jsonify, flash, request
from .forms import UploadForm
from . import app
from . import data_collect

BASIDIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=["GET", "POST"])
def index():
    form = UploadForm()
    fig = go.Figure()

    file_path = None
    if form.validate_on_submit():
        filename = data_collect.save(form.data.data)
        file_path = data_collect.path(filename)
        x, y = np.loadtxt(file_path, delimiter=',', unpack=True)
        fig.add_trace(go.Scatter(x=x, y=y, name="Исходная переходная характеристика объекта"))
        fig.update_layout(margin=dict(l=5, r=5, t=40, b=5),
                          title="Исходная переходная характеристика объекта",
                          xaxis_title="t, c",
                          yaxis_title="h(t)")
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        file_path += "/test.JSON"
        with open(file_path, 'w') as file:
            file.write(f'var graphs = {graphJSON};')
        return render_template('index.html', form=form, file_url=file_path)
    return render_template('index.html', form=form, file_url=file_path)

@app.route('/check-plotly', methods=['GET', 'POST'])
def check_plotly():
    x, y = np.loadtxt("time_value.txt", delimiter=',', unpack=True)
