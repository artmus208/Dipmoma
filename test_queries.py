from app import app
from app.models.user import Qualification, Users

with app.app_context():
    u = Users.get_by_email(
        "123@12"
    )
    if u:
        print(u.id)
