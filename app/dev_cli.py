from flask import Blueprint
from readchar import readchar
from werkzeug.security import check_password_hash, generate_password_hash

from .models.user import Users
from . import db, logger


bp = Blueprint('dev', __name__, url_prefix='/dev')

def need_confirm(label:str):
    print(f"This is dangerous operation {label.upper()}, please, confirm your intention.")
    print('Press Y')
    c = readchar()
    if c == 'Y': return True
    else: return False 
    

@bp.cli.command('recreate-db')
def create_db():
    if need_confirm('recreate-db'):
        db.drop_all()
        db.create_all()
        db.session.commit()
        logger.warning('DB models are recreated')
        print('DB models are recreated')
    else: print('reject')
    
@bp.cli.command('seed-db')
def seed_db():
    try:
        new_one = Users(
            1, "Artur",
            "Mustafin", "mustafin.2000@gmail.com",
            generate_password_hash(str(123)), "Студент",
        )
        new_one.save()
        print("Success")
    except Exception as e:
        logger.error(str(e))
        print("fail")
    