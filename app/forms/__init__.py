from flask import current_app
from flask_uploads import (
        UploadSet, configure_uploads, TEXT, patch_request_class
)

def create_upload_set():
    data_collector = UploadSet('data', TEXT)
    configure_uploads(current_app, data_collector)
    patch_request_class(current_app, None)
    return data_collector
data_collector = create_upload_set()