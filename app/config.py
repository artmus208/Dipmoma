import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MAX_CONTENT_LENGTH = 16*1024*1024
    UPLOADED_TEXT_DEST = os.path.join(basedir, 'static/data/uploads')
    UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'static/data/uploads')
    ALLOWED_EXTENSIONS = {'txt'}