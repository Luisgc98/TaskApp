# -*- coding: utf-8 -*-
from app import create_app
from flask import redirect, render_template, request, flash, url_for, make_response, session
from flask_login import login_required, current_user
from app.data_base import task_user, task_user_done, task_user_pending, delete_user_data
from app.forms import DeleteTaskForm, TaskEditForm, SearchTask, EditPassword
from datetime import datetime

app = create_app()

@app.route('/')
def index():
    	
	delete = request.args.get('id_delete', None)
	if delete is not None:
		delete_user_data(delete)
    	
	response = make_response(redirect(url_for('auth.login')))
	response.set_cookie('logout', 'False')
    	
	return response

@app.route('/home', methods=['GET', 'POST'])
@login_required
def Home():
    	
	username = current_user.user_name
	tasks = task_user(current_user.id)
	delete = DeleteTaskForm()
	edit_form = TaskEditForm()
	search_form = SearchTask()

	dates = {
		'username':username,
		'tasks': tasks,
		'delete': delete,
		'edit_form': edit_form,
		'search_form': search_form,
		'pag': 'Home'
	}
    	
	return render_template('home.html', **dates)

@app.route('/profile', methods=['GET', 'POST'])
def profile():

	id = current_user.id
	username = current_user.user_name
	email = current_user.email
	passwd = current_user.password
	init_date = current_user.init_date
	num_tasks = len(task_user(current_user.id))
	tasks_done = len(task_user_done(current_user.id))
	tasks_pending = len(task_user_pending(current_user.id))
	edit_password = EditPassword()

	dates = {
		'id': id,
		'username':username,
		'email':email,
		'password':passwd,
		'init_date':init_date,
		'num_tasks': num_tasks,
		'tasks_done': tasks_done,
		'tasks_pending': tasks_pending,
		'edit_password': edit_password,
		'upd': request.cookies.get('upd'),
		'pag': 'profile'
	}	
	return render_template('profile.html', **dates)

@app.errorhandler(400)
def erno_400(error):
	dates = {
		'error': error,
	}
	
	return render_template('400.html', **dates)

@app.errorhandler(404)
def erno_404(error):
	dates = {
		'error': error,
	}

	return render_template('404.html', **dates)

@app.errorhandler(500)
def erno_500(error):
	dates = {
		'error': error,
	}

	return render_template('500.html', **dates)

@app.errorhandler(503)
def erno_503(error):
	dates = {
		'error': error,
	}

	return render_template('503.html', **dates)

@app.errorhandler(504)
def erno_504(error):
	dates = {
		'error': error,
	}

	return render_template('504.html', **dates)

if __name__=='__main__':
	app.run(debug=True, port=8000)