from flask import render_template, redirect, url_for, request, flash
from datetime import datetime as current_date
from . import auth
from app.forms import LoginForm, SignUpForm
from app.database import users

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
    if 'signup_submit' in request.form:
        user_name = signup_form.names.data.strip()+' '+signup_form.surnames.data.strip()
        password = signup_form.new_password.data.strip()
        email = signup_form.email.data.strip()
        area = signup_form.area.data.strip()
        init_date = current_date.now().date()
        new_user = users(
            user_name=user_name,
            password=password,
            email=email,
            area=area,
            init_date=init_date
        )
        message = users.add_user(new_user=new_user)
        print(message)

    return redirect(url_for('auth.login'))