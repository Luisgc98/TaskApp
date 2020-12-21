from flask import render_template
from . import main
from app.database import tasks

@main.route('/home', methods=['GET', 'POST'])
def home():
    list_tasks = tasks.get_all_tasks()

    return render_template('home.html', list_tasks=list_tasks)