from flask import render_template, redirect, url_for, request, flash
from datetime import datetime as current_date
from . import auth
from app.forms import LoginForm, SignUpForm
from app.database import users
from app.mail_senders import mail_sender_wel

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    signup_form = SignUpForm()
    
    if login_form.validate_on_submit() \
        and 'login_submit' in request.form:
        print(request.form)

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
        exist = False
        email = signup_form.email.data.strip()
        for user in list_users:
            if email == user.email: 
                exist = True
        if exist:
            flash('Usuario ya registrado con esta cuenta.')
        else:
            password = signup_form.new_password.data.strip()
            user_name = signup_form.names.data.strip()+' '+signup_form.surnames.data.strip()
            area = signup_form.area.data.strip()
            init_date = current_date.now().date()
            new_user = users(
                user_name=user_name,
                password=password,
                email=email,
                area=area,
                init_date=init_date
            )
            send_mail = mail_sender_wel(email=email, user_name=user_name, password=password)
            message = users.add_user(new_user=new_user)
            flash(message)
            flash(send_mail)

    return redirect(url_for('auth.login'))