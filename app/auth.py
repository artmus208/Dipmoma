from flask import(
    redirect, render_template, url_for, 
    jsonify, flash, request, g, session, Blueprint
)
from werkzeug.security import(
    check_password_hash, generate_password_hash
)
from .forms.register_form import RegisterForm
from .db import get_db

bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/register', methods=('GET', 'POST'))
def register():
    form:RegisterForm = RegisterForm()
    form.position.choices = [
        (-1, "Вид деятельности:"),
        ("Студент"),
        ("Инженер"),
        ("Преподаватель"),
        ("Специалист по идентификации"),
        ("Другое...")
    ]
    if form.validate_on_submit():
        db = get_db()
        position = form.position.data
        if position == "Другое...":
            position = form.other.data
        try:
            db.execute(
                'INSERT INTO user (f_name, s_name, mail, password, position)'
                'VALUES (?, ?, ?, ?, ?)',
                (form.first_name.data, form.second_name.data, 
                 form.mail.data, form.password.data, 
                 position)
            )
        except db.IntegrityError:
            error = f"Пользователь с почтой {form.mail.data} уже зарегистрирован"
        else:
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')


@bp.route("/login", methods=('GET', 'POST'))
def login():
    pass