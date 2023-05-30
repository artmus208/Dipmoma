import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app
from . import logger
from .utils.decorators import login_required
bp = Blueprint("ident", __name__, url_prefix='/ident')


@bp.route('/')
def index():
    return render_template("ident/new_index.html")



