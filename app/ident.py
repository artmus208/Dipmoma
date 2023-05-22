import os
import json
import plotly
import numpy as np
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.graph_objects as go
import control as co

from flask import(
    redirect, render_template, url_for, jsonify, flash, request, g, session, Blueprint
)
from .forms.ident_form import IdentForm
from .forms.upload_form import UploadForm

from . import data_collect
from .ident_methods import LSM

from .utilities import tex2svg

BASEDIR = os.path.abspath(os.path.dirname(__file__))

bp = Blueprint('ident', __name__)

@bp.route('/', methods=["GET", "POST"])
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
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            session["x"] = x.tolist()
            session["y"] = y.tolist()
            g.x = x.tolist()
            return render_template('index.html', 
                                   ident_form=ident_form, 
                                   form=form, 
                                   graph_json=graphJSON)
        return render_template('index.html', form=form, file_url=file_path)
    except Exception as e:
        flash("Exception on index")
        return redirect(url_for("index"))

# TIPS:
# [ ]: все проверки передачи данных можно делать в декораторе
# [ ]: работу с перехватом эксепшинов можно перевести в декораторы
@bp.route('/system-ident', methods=['GET', 'POST'])
def system_ident():
    form = IdentForm(request.form)
    x, y = session.get("x", None), session.get("y", None)
    if x is None or y is None:
        flash(f'/system-ident: x is None or y is None')
        return redirect(url_for('index'))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Исходная ПХ"))
    num, den = LSM(x, y, form.degree.data)
    dpf = co.tf(num, den, x[1]-x[0])
    x_dpf, y_dpf = co.step_response(dpf, T = 1)
    fig.add_trace(go.Scatter(x=x_dpf, y=y_dpf, name="Идент. МНК"))
    fig.update_layout(
        title="Идентифицировались",
        xaxis_title="t, c",
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # LaTex to SVG procedure
    svg_str = tex2svg(dpf._repr_latex_()[1:-1])
    with open(BASEDIR+'/static/img/tf.svg', 'w') as f:
        f.write(svg_str)

    return render_template('system_ident.html', graph_json=graphJSON)




@bp.route('/check-plotly', methods=['GET', 'POST'])
def check_plotly():
    x, y = np.loadtxt("time_value.txt", delimiter=',', unpack=True)