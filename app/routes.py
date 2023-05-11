from . import logger
from flask import redirect, render_template, url_for, jsonify, flash, request
from .forms import UploadForm
from . import app
from . import data_collect

import json
import plotly
import numpy as np
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.graph_objects as go

@app.route('/', methods=["GET", "POST"])
def index():
    form = UploadForm()
    x = []
    y = []
    graphJSON = None
    file_url = None
    if form.validate_on_submit():
        filename = data_collect.save(form.data.data)
        file_url = data_collect.url(filename)
    else:
        file_url = None
    try:
        with open("../uploads/data/time_value_5.txt") as f:
            for line in f:
                x_, y_ = line.split(',')
                x.append(float(x_))
                y.append(float(y_))
    except Exception as e:
        logger.warning(f"index: {e}")
        redirect(url_for("index"))
    fig = make_subplots(rows=1, cols=1, subplot_titles=("Переходная характеристика"), 
                        shared_xaxes=True, vertical_spacing=0.1)
    fig.append_trace(go.Scatter(x = x, y = y, name = 'Переходной процесс'), row=1, col=1)
    fig.update_traces(hovertemplate=None)
    layout={'hovermode': 'x', "height":800}
    fig.update_layout(layout)
    graphJSON = pio.to_json(fig) 

    return render_template('index.html', form=form, file_url=file_url, chart=graphJSON)

@app.route('/check-plotly', methods=['GET', 'POST'])
def check_plotly():
    x, y = np.loadtxt("time_value.txt", delimiter=',', unpack=True)
