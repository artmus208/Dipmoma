from flask import Blueprint
from flask import current_app as app

bp = Blueprint("base", __name__)

@bp.route('/hello')
def hello():
    app.logger.debug("A debug message")
    app.logger.info("An info message")
    app.logger.warning("A warning message")
    app.logger.error("An error message")
    app.logger.critical("A critical message")
    return 'Hello, World!'

