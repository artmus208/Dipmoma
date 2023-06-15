import functools
import os
import numpy as np
from flask import (
    Blueprint, Response, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for
)
from flask import current_app as app
from werkzeug.utils import secure_filename

from . import logger
from .utils.decorators import login_required
from .utils.identify_it import IdentifyIt

bp = Blueprint("ident", __name__, url_prefix='/ident')


@bp.route('/')
def index():
    return render_template("ident/new_index.html")


@bp.route('/handler', methods=("GET", "POST"))
def methods():
    # TIPS Сделать это потом декоратором:
    if not session.get('last_filepath', False):
        # TIPS Лучше конечно на клиенте тоже проверять загрузку файла
        flash('Файл не загружен')
        return redirect(url_for('ident.index'))
    data = request.get_json()
    degree = int(data['degree'])
    method_id = int(data["method_id"])
    # Тут нужно обработать входные данные
    x, y = np.loadtxt(session["last_filepath"], delimiter=',', unpack=True)
    ident = IdentifyIt(x, y, degree, method_id)
    y_m = ident.y_m
    x_m = ident.x_m
    resp_data = {
        'x1':x.tolist(),
        'y1':y.tolist(),
        'x2':x_m.tolist(),
        'y2':y_m.tolist(),
        'error': float(ident.error),
        'tf_formula': ident.model._repr_latex_(),
    }
    return jsonify(resp_data)


@bp.route('/u', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('Нет файла')
        return redirect(url_for("ident.index"))
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('Файл не выбран')
        return redirect(url_for("ident.index"))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session['last_filepath'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        flash(f'Файл {filename} успешно загружен!')
    return redirect(url_for("ident.index"))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
