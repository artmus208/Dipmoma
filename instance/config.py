
from flask import url_for
import os

SQLALCHEMY_DATABASE_URI = "{connectorname}://{username}:{password}@{hostname}/{databasename}".format(
            connectorname="mariadb+mariadbconnector",
            username="root",
            password="pesk-2020",
            hostname="127.0.0.1:3306",
            databasename="ident",
            )
SECRET_KEY = 'dev'
# UPLOAD_FOLDER = 'D:/semester8/Diploma/app/static/uploads'
UPLOAD_FOLDER = os.path.join(os.getcwd(), "app", "static", "uploads")
ALLOWED_EXTENSIONS = {'txt', 'csv'}