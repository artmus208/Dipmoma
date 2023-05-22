import logging
import os
from flask import Flask
from flask_uploads import (
        UploadSet, configure_uploads, TEXT, patch_request_class
    )
from .config import Config


def create_app(test_config=None):
    """application factory"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "ident.sqlite")
    )
    app.config.from_object(Config)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)
    return app


app = create_app()

from . import auth
app.register_blueprint(auth.bp)
from . import ident
app.register_blueprint(ident.bp)
app.add_url_rule('/', endpoint='index')
def create_upload_set():
    data_collector = UploadSet('data', TEXT)
    configure_uploads(app, data_collector)
    patch_request_class(app, None)
    return data_collector
data_collector = create_upload_set()
