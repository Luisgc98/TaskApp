# -*- coding: utf-8 -*-
from . import auth
from flask import session, redirect, render_template, flash, url_for, request, make_response
from app.forms import UserForm, NewUserForm
from app.data_base import Users, user_data_by_email, signup_user
from app.config import Config
from app.models import UserDates, ModelUser
from app.emails import email_message
from flask_mail import Message
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from validate_email import validate_email

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = UserForm()
    logout = request.cookies.get('logout')

    dates = {
        'login_form': login_form,
        'logout': logout
    }
    
    if login_form.validate_on_submit():
    	email = login_form.email.data.strip()
        passwd = login_form.password.data

        user_validate = user_data_by_email(id_user=email)
        if user_validate is not None:
            passwd_db = check_password_hash(
                pwhash=user_validate.password,
                password=passwd
            )
            if passwd_db:
                dates_usu = UserDates(
                    id=user_validate.id,
                    user_name=user_validate.user_name,
                    password=passwd,
                    init_date=user_validate.init_date,
                    email = user_validate.email
                )
                user = ModelUser(dates_usu)
                login_user(user)
                Config.SECRET_KEY = current_user.password
                session['username'] = current_user.user_name
                flash('User logged in successfully. Welcome {}'.format(user_validate.user_name))
                return redirect(url_for('Home'))
            else:
                print(passwd_db)
                response = make_response(redirect(url_for('auth.login')))
                response.set_cookie('logout', 'False')
                flash('Incorrect Data. Please, check and try again.')
                return response
        else:
            response = make_response(redirect(url_for('auth.login')))
            response.set_cookie('logout', 'False')
            flash('User not found.')
            return response
    
    return render_template('index.html', **dates)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    signup_form = NewUserForm()

    dates = {
        'signup_form': signup_form,
    }
    
    if request.method == 'POST':
        email = request.form['email'].encode('utf8')
    	username = request.form['username'].encode('utf8')
        passwd = request.form['password'].encode('utf8')
        confirmation = request.form['password_confirmation'].encode('utf8')

        user_validate = user_data_by_email(id_user=email)
        if user_validate is None:
            if validate_email(email, verify=True):
                if len(username.split('.')) > 1 and len(username.split('.')) < 3:
                    alphanumeric = passwd.isalnum() # True
                    alphabetic = passwd.isalpha() # False
                    numeric = passwd.isdigit() # False
                    lower = passwd.islower() # False
                    upper = passwd.isupper() # False
                    if alphanumeric and not alphabetic and not numeric and not lower and not upper:
                        if passwd == confirmation:
                            passwd_db = generate_password_hash(passwd)
                            user_dates = Users(
                                user_name=username, 
                                password=passwd_db, 
                                init_date=str(datetime.now().date()),
                                email=email
                            ),
                            user_dates = user_dates[0]
                            signup_user(user_dates)
                            validate = user_data_by_email(id_user=email)
                            email_message(username, email, passwd)
                            dates_usu = UserDates(
                                id=validate.id,
                                user_name=validate.user_name,
                                password=validate.password,
                                init_date=validate.init_date,
                                email=validate.email
                            )
                            user = ModelUser(dates_usu)
                            login_user(user)
                            Config.SECRET_KEY = passwd
                            session['username'] = username
                            flash('User logged in successfully. Welcome {}'.format(username))
                            return redirect(url_for('Home'))
                        else:
                            flash('Signup failed.'.decode('utf8'))
                            flash('Passwords do not match.'.decode('utf8'))
                    else:
                        flash('Signup failed.'.decode('utf8'))
                        flash('Invalid password'.decode('utf8'))
                else:
                    flash('Signup failed.'.decode('utf8'))
                    flash('Invalid username'.decode('utf8'))
            else:
                flash('Signup failed.'.decode('utf8'))
                flash('No email exists.'.decode('utf8'))
        else:
            flash('User already exists.')
    
    return render_template('signup.html', **dates)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Come back soon!')

    response = make_response(redirect(url_for('auth.login')))
    response.set_cookie('logout', 'True')
    return response