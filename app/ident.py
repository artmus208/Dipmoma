import functools
import os
from flask import (
    Blueprint, flash, g, make_response, redirect, render_template, request, session, url_for
)
from flask import current_app as app
from werkzeug.utils import secure_filename

from . import logger
from .utils.decorators import login_required
bp = Blueprint("ident", __name__, url_prefix='/ident')


@bp.route('/')
def index():
    return render_template("ident/new_index.html")


@bp.route('/handler', methods=("GET", "POST"))
def methods():
    data = request.get_json()
    degree = data['degree']
    method_id = int(data["method_id"])
    session["degree"] = degree
    session["method_id"] = method_id
    response = make_response('', 200)
    return response


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
        logger.info(f'Last upload filepath:\n{session["last_filepath"]}')

        flash(f'Файл {filename} успешно загружен!')
    return redirect(url_for('ident.index'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
