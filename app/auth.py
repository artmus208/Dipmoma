import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from . import logger

from .forms.log_form import LoginForm
from .forms.reg_form import RegisterForm
from .models.user import Users, Qualifications


bp = Blueprint("auth", __name__, url_prefix='/auth')

# DONE:
# [x]: checkout about register https://proproprogs.ru/flask/registraciya-polzovateley-i-shifrovanie-paroley
@bp.route('/register', methods=('GET', 'POST'))
def register():
    form:RegisterForm = RegisterForm(quals=Qualifications.get_ids_names())
    if request.method == "POST":
        if form.validate_on_submit():
            newbee = Users(
                first_name=form.first_name.data,
                second_name=form.second_name.data,
                email=form.mail.data,
                password=generate_password_hash(form.password.data),
                qualification_id=int(form.qual.data),
            )
            try:
                newbee.save()
            except IntegrityError as e:
                form.mail.errors.append("Электронная почта уже зарегистрирована, введите другую")
                flash("Ошибка при регистрации")
                return render_template('auth/register.html', form=form)    
            
            flash('Успешная регистрация')
            return redirect(url_for('auth.login'))
        
        else:
            flash("Ошибка при регистрации")
            return render_template('auth/register.html', form=form)   
             
    return render_template('auth/register.html', form=form)

# DONE:
# [x]: checkout about login https://proproprogs.ru/flask/avtorizaciya-polzovateley-na-sayte-cherez-flask-login
@bp.route('/login', methods=('GET', 'POST'))
def login():
    form:LoginForm = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            usermail = form.mail.data
            password = form.password.data
            user:Users = Users.get_by_email(usermail)
            if not user:
                form.mail.errors.append("Пользователь с этим адресом не зарегистрирован")
                form.password.data = ""       
                return render_template('auth/login.html', form=form)
            
            if not check_password_hash(user.password, password):
                form.password.errors.append('Некорректный пароль')
                form.password.data = ""  
                return render_template('auth/login.html', form=form)
            
            session['user_id'] = user.id
            return redirect(url_for('ident.index'))
        
    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = Users.get(user_id)
    pass

@bp.route('/hello')
def hello():
    logger.info("Hello")
    return 'Hello, World!'
