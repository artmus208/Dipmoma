import logging

from flask import Flask
from flask_uploads import (
        UploadSet, configure_uploads, TEXT, patch_request_class
    )
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s:%(name)s:%(levelname)s:%(message)s'
    )
    file_handler = logging.FileHandler('iDentWebApp.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

app = create_app()
logger = create_logger()
def create_upload_set():
    data_collector = UploadSet('data', TEXT)
    configure_uploads(app, data_collector)
    patch_request_class(app, None)
    return data_collector

data_collect = create_upload_set()
from . import routes