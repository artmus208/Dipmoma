import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '8b2771f9bdfgdfgw186123sdfsf749ccadad43'
    MAX_CONTENT_LENGTH = 16*1024*1024
    UPLOADED_TEXT_DEST = os.path.join(basedir, 'static/data/uploads')
    UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'static/data/uploads')
    ALLOWED_EXTENSIONS = {'txt'}