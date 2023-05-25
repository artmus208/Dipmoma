from flask import Blueprint
from flask import current_app as app

from . import logger
bp = Blueprint("base", __name__)

@bp.route('/hello')
def hello():
    logger.debug(f"A debug message ", extra={"func":"hello func"})
    logger.info("An info message", extra={"func":"hello func"})
    logger.warning("A warning message", extra={"func":"hello func"})
    logger.error("An error message", extra={"func":"hello func"})
    logger.critical("A critical message", extra={"func":"hello func"})

    logger.info(f'{app.secret_key}', extra={"func":"hello"})
    return 'Hello, World!'

