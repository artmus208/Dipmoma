import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app
from . import logger

from .forms.log_form import LoginForm
from .forms.reg_form import RegisterForm


bp = Blueprint("auth", __name__, url_prefix='/auth')

# TODO:
# [ ]: checkout about register https://proproprogs.ru/flask/registraciya-polzovateley-i-shifrovanie-paroley
@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)

# TODO:
# [ ]: checkout about login https://proproprogs.ru/flask/avtorizaciya-polzovateley-na-sayte-cherez-flask-login
@bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.html'))

@bp.before_app_request
def load_logged_in_user():
    # user_id = session.get('user_id')

    # if user_id is None:
    #     g.user = None
    # else:
    #     g.user = get_db().execute(
    #         'SELECT * FROM user WHERE id = ?', (user_id,)
    #     ).fetchone()
    pass

@bp.route('/hello')
def hello():
    logger.info("Hello")
    return 'Hello, World!'
