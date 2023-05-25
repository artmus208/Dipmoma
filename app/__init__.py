import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s | %(module)s]:%(message)s",
                "datefmt": "%d.%m.%y %H:%M:%S",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "app.log",
                "formatter": "default",
            },
        },
        "root": {"level": "WARNING", "handlers": ["console", 'file']},
    }
)

db = SQLAlchemy()

def create_app(test_config=None):
    """application factory"""
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
   
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    app.add_url_rule('/', endpoint='index')
    return app

