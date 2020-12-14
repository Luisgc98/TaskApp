from flask import render_template
from . import auth
from app.forms import LoginForm, SignUpForm
from app.database import users

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    signup_form = SignUpForm()
        
    dates = {
        'login_form': login_form,
        'signup_form': signup_form,
    }
    
    return render_template('index.html', **dates)