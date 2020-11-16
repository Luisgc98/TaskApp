# -*- coding: utf-8 -*-
from werkzeug.utils import redirect
from . import record
from app.forms import TaskForm, DeleteTaskForm, TaskEditForm, SearchTask
from app.data_base import Tasks, add_task, task_user, delete_task, status_task, edit_task, update_password, update_username, update_email, delete_user_data
from app.emails import email_change_passwd, email_change_email
from flask import render_template, flash, request, make_response, url_for
from flask_login import login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

@record.route('/addtask', methods=['GET', 'POST'])
@login_required
def addtask():
    task_form = TaskForm()
    username = current_user.user_name
    record = request.cookies.get('record')

    dates = {
        'task_form': task_form,
        'username': username,
        'record': record
    }

    if task_form.validate_on_submit():
        task_name = task_form.task_name.data.encode('utf-8')
        task = task_form.task.data
        if len(task_name) < 50 and len(task) < 1000:
            action = None
            tasks = task_user(current_user.id)
            if tasks == []:
                action = True
            else:
                for task_usu in tasks:
                    if task_name.decode('utf8') == task_usu.task_name:
                        action = False
                        break
                    elif task_name.decode('utf8') != task_usu.task_name:
                        action = True

            if action:
                if '"' in task:
                    task = task.replace('"', "'")
                if '\r' in task.encode('utf8') or '\n' in task.encode('utf8'):
                    task = task.encode('utf8').replace('\r', " ")
                    task = task.encode('utf8').replace('\n', " ")
                taskdate = Tasks(
                    task_name=task_name,
                    task = task
                )
                add_task(taskdate)
                response = make_response(redirect(url_for('record.addtask')))
                response.set_cookie('record', 'True')
                flash('Task added successfully.')
                return response
            else:
                response = make_response(redirect(url_for('record.addtask')))
                response.set_cookie('record', 'False')
                flash('Error. Existing task.')
                return response
        else: 
            response = make_response(redirect(url_for('record.addtask')))
            response.set_cookie('record', 'False')
            flash('Invalid task. Too many characters.')
            return response

    return render_template('addtask.html', **dates)

@record.route('/home/delete/<task>/<pag>', methods=['GET', 'POST'])
@login_required
def deletetask(task, pag):
    delete_task(task)
    search = request.cookies.get('search')

    flash('Delete successfully.'.decode('utf-8'))
    response = make_response(redirect(url_for(pag.encode('utf8'), search=search)))
    return response

@record.route('/home/status/<task>/<pag>', methods=['GET', 'POST'])
@login_required
def status(task, pag):
    status_task(task)
    search = request.cookies.get('search')

    flash('Task status updated.')
    response = make_response(redirect(url_for(pag.encode('utf8'), search=search)))
    return response

@record.route('/home/edittask/<task>/<pag>', methods=['GET', 'POST'])
@login_required
def edittask(task, pag):
    if request.method == 'POST':
        vocales = ['a', 'e', 'i', 'o', 'u', "'"]
        for i in range(len(task)):
            if task[i] == u'\ufffd':
                if str(task[i+1]) in vocales:
                    task = task.replace(task[i], u'ñ')
                    break
                if str(task[i+1]) not in vocales:
                    task = task.replace(task[i], u'ó')
                    break

    name = request.form['task_name'].encode('utf8')
    content = request.form['task'].encode('utf8')
    new_content = ''
    if '\r' in content or '\n' in content:
        content = content.replace('\r', " ")
        content = content.replace('\n', " ")
    for i in range(len(content)):
        new_content += content[i]
    edit_task(id_task=task, name=name, content=new_content)
    search = request.cookies.get('search')

    flash('Updated task.')
    response = make_response(redirect(url_for(pag.encode('utf8'), search=search)))
    return response

@record.route('/home/searchtask/<search>', methods=['GET', 'POST'])
@login_required
def searchtask(search):
    months = ['junary', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    search = search.encode('utf8').lower().strip()
    tasks = task_user(current_user.id)
    results = []
    for i in tasks:
        if search in i.task_name.lower():
            results.append(i)
        elif search == 'pending' or search == 'pendiente' or search == 'pendientes' or search == 'faltantes':
            if i.status == False:
                results.append(i)
        elif search == 'done' or search == 'realizadas' or search == 'echas':
            if i.status == True:
                results.append(i)
        elif search in months:
            month = str(months.index(search)+1) if len(months.index(search)+1) > 1 else '0'+str(months.index(search)+1)
            if month in i.task_date.encode('utf8').split('-')[1]:
                results.append(i)
        elif search in meses:
            mes = str(meses.index(search)+1) if len(str(meses.index(search)+1)) > 1 else '0'+str(meses.index(search)+1)
            if mes in i.task_date.encode('utf8').split('-')[1]:
                results.append(i)
        elif search in i.task_date:
            results.append(i)

    username = current_user.user_name
    delete = DeleteTaskForm()
    edit_form = TaskEditForm()
    search_form = SearchTask()

    dates = {
		'username':username,
		'tasks_results': results,
		'delete': delete,
		'edit_form': edit_form,
		'search_form': search_form,
        'pag':'record.searchtask'
	}

    response = make_response(render_template('search.html', **dates))
    response.set_cookie('search', search)
    return response

@record.route('/profile/editpasswd/<current>/<new>/<confir>', methods=['GET', 'POST'])
@login_required
def editpasswd(current, new, confir):
    action = 'False'
    if current != new:
        passwd_db = check_password_hash(
            pwhash=current_user.password,
            password=current
        )
        if passwd_db:
            alphanumeric = new.isalnum() # True
            alphabetic = new.isalpha() # False
            numeric = new.isdigit() # False
            lower = new.islower() # False
            upper = new.isupper() # False
            if alphanumeric and not alphabetic and not numeric and not lower and not upper:
                if new == confir:
                    passwd_db = generate_password_hash(new)
                    if update_password(id_user=current_user.id, new_pass=passwd_db):
                        response = make_response(redirect(url_for('profile')))
                        response.set_cookie('upd', 'True')
                        current_user.password = passwd_db
                        email_change_passwd(current_user.user_name, current_user.email, new)
                        flash('Password updated successfully.'.decode('utf8'))
                        flash('An email has been sent to: {} with your updated password.'.format(current_user.email).decode('utf8'))
                        return response
                    else:
                        flash('Something happened. Please try again later.'.decode('utf8'))
                else:
                    flash('Update failed.'.decode('utf8'))
                    flash('Passwords do not match.'.decode('utf8'))
            else:
                flash('Update failed.'.decode('utf8'))
                flash('Invalid password'.decode('utf8'))
        else:
            flash('Current Password Incorrect.')
    else: 
        flash('The new password cannot match the current password.'.decode('utf8'))

    response = make_response(redirect(url_for('profile')))
    response.set_cookie('upd', action)
    return response

@record.route('/profile/editprofile/<name>/<mail>', methods=['GET', 'POST'])
@login_required
def editprofile(name, mail):
    action = 'False'
    if len(name.split('.')) > 1 and len(name.split('.')) < 3:
        if name != current_user.user_name and name != '':
            update_username(id_user=current_user.id, name=name.strip())
            current_user.user_name = name.strip()
            response = make_response(redirect(url_for('profile')))
            response.set_cookie('upd', 'True')
            flash('Username updated successfully.'.decode('utf8'))
            return response
    else:
        flash('Inavlid Username'.decode('utf8'))
        flash('Note: The username must have two names separated by a period (user.name)'.decode('utf8'))

    if mail.stri().split('@')[1] == 'gmail.com':
         if mail.strip() != current_user.email and  mail != '':
            update_email(id_user=current_user.id, mail=mail)
            current_user.email = mail
            email_change_email(username=current_user.user_name, new_email=mail, passwd=current_user.password)
            response = make_response(redirect(url_for('profile')))
            response.set_cookie('upd', 'True')
            flash('E-mail updated successfully.'.decode('utf8'))
            flash('An email has been sent to: {} with your updated details.'.format(current_user.email).decode('utf8'))
            return response
    else:
        flash('Invalid E-mail.'.decode('utf8'))
        flash('It should be @gmail'.decode('utf8'))

    response = make_response(redirect(url_for('profile')))
    response.set_cookie('upd', action)
    return response

@record.route('/profile/deleteuser/<user>', methods=['GET', 'POST'])
@login_required
def deleteuser(user):
    logout_user()
    delete_user_data(user)
    flash('User deleted successfully.'.decode('utf8'))
    
    response = make_response(redirect(url_for('index')))
    return response