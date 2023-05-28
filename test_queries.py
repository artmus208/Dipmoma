from app import app
from app.models.user import Qualifications, Users

# with app.app_context():
#     u = Users.get_by_email(
#         "123@12"
#     )
#     if u:
#         print(u.id)


# with app.app_context():
#     q = Qualifications(1, "Студент")
#     q.save_to_file("quals.csv")

#     Q = Qualifications(2, "Преподаватель")
#     Q.save_to_file("quals.csv")

#     q2 = Qualifications(3, "Специалист в ИС")
#     q2.save_to_file("quals.csv")


# with app.app_context():
#     q = Qualifications()
#     res = q.load_from_file('quals.csv')
#     print(res)