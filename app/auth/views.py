from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from app.forms import LoginForm, SignUpForm
from app.database import users
from validate_email import validate_email

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    signup_form = SignUpForm()
    
    if login_form.validate_on_submit() \
        and 'login_submit' in request.form:
        login = login_form.validate_user()
        if login == False:
            flash('Contraseña incorrecta.')
        elif login == None:
            flash('Correo o Nombre de Usuario incorrecto.')
            return redirect(url_for('auth.login'))
        else:
            role = login_form.validate_role(user=login)
            if role:
                flash(f'Bienvenido {login.user_name}')
                return redirect(url_for('main.home'))
            else:
                flash('Rol aún asignado. Consulte con su Coach para mas información.')
            
    dates = {
        'login_form': login_form,
        'signup_form': signup_form,
    }
    
    return render_template('index.html', **dates)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignUpForm()
    list_users = users.all_users()
    if 'signup_submit' in request.form:
        signup = signup_form.validate_signup(list_users)
        if signup == False:
            flash('Usuario ya registrado con este correo.')
        else:
            if validate_email(signup.email, verify=True):
                message = users.add_user(new_user=signup)
                send_mail = signup_form.send_mail(email=signup.email, user_name=signup.user_name, password=signup_form.new_password)
                flash(message)
                flash(send_mail)
            else:
                flash('Verifique que su Correo sea correcto.')

    return redirect(url_for('auth.login'))

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Que vuelva pronto.')

    return redirect(url_for('auth.login'))