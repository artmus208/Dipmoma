import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app
from . import logger


bp = Blueprint("auth", __name__, url_prefix='/auth')

@bp.route('/hello')
def hello():
    logger.info("An info message", extra={"func":"hello"})
    return 'Hello, World!'

@bp.route('/show-time')
def show_time():
    logger.info(str(app.import_name), extra={"func":"show_time"})
    return redirect(url_for('auth.hello'))


@bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.html')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.html'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
