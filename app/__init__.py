import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s in %(module)s.%(funcName)s:%(lineno)d] '%(message)s'",
                "datefmt": "%d.%m.%y %H:%M:%S",
            },
            "minimum": {
                "format": "%(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "minimum",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "app.log",
                "formatter": "default",
            },
        },
        "loggers": {
            "extra": {
                "level": "DEBUG",
                "handlers": ["file"],
                "propagate": False,
            }
        },
    }
)

logger = logging.getLogger('extra')

db = None

def create_app(test_config=None):
    global db
    """The Application factory"""
    app = Flask(__name__, instance_relative_config=True)    
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    _db = SQLAlchemy()
    _db.init_app(app)

    db = _db
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import ident
    app.register_blueprint(ident.bp)

    from . import dev_cli
    app.register_blueprint(dev_cli.bp)
    app.add_url_rule('/', endpoint='ident.index')
    app.add_url_rule('/hello', endpoint='auth.hello')
    
    from .models import user
    return app

app = create_app()