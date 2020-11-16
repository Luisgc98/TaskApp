from . import SQLAlchemy
from datetime import datetime
from flask_login import current_user

# Base de Datos de los Usuarios

db = SQLAlchemy()

class Users(db.Model):
	__tablename__= 'users'
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.Unicode)
	password = db.Column(db.Unicode)
	init_date = db.Column(db.Unicode)
	email = db.Column(db.String)

	def __init__(self, user_name, password, init_date, email):
    		
		self.user_name = user_name
		self.password = password
		self.init_date = init_date
		self.email = email

def all_users():
	users = Users.query.all()
	return users

def user_data_by_email(id_user):
	user = Users.query.filter_by(email=id_user).first()
	return user

def user_data_by_username(id_user):
	user = Users.query.filter_by(user_name=id_user).first()
	return user

def user_data_by_id(id_user):
	user = Users.query.filter_by(id=id_user).first()
	return user

def signup_user(dates):
    try:
        db.session.add(dates)
        db.session.commit()
        return True
    except: return False

def update_password(id_user, new_pass):
	try:
		user = Users.query.filter_by(id=id_user).first()
		new_password = new_pass
		user.password = new_password
		db.session.commit()
		return True
		
	except: return False

def update_username(id_user, name):
	try:
		user = Users.query.filter_by(id=id_user).first()
		new_username = name
		user.user_name = new_username
		db.session.commit()
		return True
		
	except: return False

def update_email(id_user, mail):
	try:
		user = Users.query.filter_by(id=id_user).first()
		new_mail = mail
		user.user_name = new_mail
		db.session.commit()
		return True
		
	except: return False


# Base de Datos de las Tareas.

class Tasks(db.Model):
	__tablename__= 'tasks'
	id = db.Column(db.Integer, primary_key=True)
	task_id = db.Column(db.Integer)
	task_name = db.Column(db.String)
	task = db.Column(db.String)
	task_date = db.Column(db.Unicode)
	status = db.Column(db.Unicode)

	def __init__(self, task_name, task):
    		
		self.task_id = current_user.id
		self.task_name = task_name
		self.task = task
		self.task_date = str(datetime.now().date())
		self.status = False

def all_tasks():
	tasks = Tasks.query.all()
	return tasks

def task_user(id_user):
	tasks = Tasks.query.filter_by(task_id=id_user).order_by(Tasks.task_name).all()
	return tasks

def task_user_done(id_user):
	tasks = Tasks.query.filter_by(task_id=id_user, status=True).all()
	return tasks

def task_user_pending(id_user):
	tasks = Tasks.query.filter_by(task_id=id_user, status=False).all()
	return tasks

def uni_task_user(id_task):
	tasks = Tasks.query.filter_by(id=id_task).first()
	return tasks

def add_task(dates):
    try:
        db.session.add(dates)
        db.session.commit()
        return True
    except: return False

def delete_task(id_task):
	try:
		delete = Tasks.query.filter_by(id=id_task).first()
		db.session.delete(delete)
		db.session.commit()
		return True
		
	except: return False

def status_task(id_task):
	try:
		task = Tasks.query.filter_by(id=id_task).first()
		status = task.status
		task.status = False if status else True
		db.session.commit()
		
		return True

	except: return False

def edit_task(id_task, name, content):
	try:
		task = Tasks.query.filter_by(id=id_task).first()
		new_task_name = name
		new_task_data = content
		if new_task_name != '':
			task.task_name = new_task_name
			db.session.commit()
		if new_task_data != '':
			task.task = new_task_data
			db.session.commit()
		return True
		
	except: return False


def delete_user_data(id_user):
	try:
		while len(task_user(id_user)) > 0:
			task_delete = Tasks.query.filter_by(task_id=id_user).first()
			db.session.delete(task_delete)
			db.session.commit()

		delete_user = Users.query.filter_by(id=id_user).first()
		db.session.delete(delete_user)
		db.session.commit()
		return True
	
	except: return False