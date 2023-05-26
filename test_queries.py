from app import app
from app.models.user import Qualification

with app.app_context():
    for q in Qualification.get_ids_names():
        print(q)
