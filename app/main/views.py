from flask import render_template
from . import main

@main.route('/home', methods=['GET', 'POST'])
def home():

    return render_template('home.html')