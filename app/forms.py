# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

validators = [DataRequired()]

class UserForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password'.decode('utf8'), validators=validators)
    submit = SubmitField(label='Enter')

class NewUserForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    username = StringField(label='New username', validators=validators)
    password = PasswordField(label='New password'.decode('utf8'), validators=validators)
    password_confirmation = PasswordField(label='Password confirmation'.decode('utf8'), validators=validators)
    submit = SubmitField(label='Sign')

class TaskForm(FlaskForm):
    task_name = StringField(label='Task Title', validators=validators)
    task = TextAreaField(label='Description'.decode('utf8'), validators=validators)
    submit = SubmitField(label='Add Task')

class TaskEditForm(FlaskForm):
    task_name = StringField(label='Task Title', )
    task = TextAreaField(label='Description'.decode('utf8'))
    savetask = SubmitField(label='Save')

class DeleteTaskForm(FlaskForm):
    deletetask = SubmitField(label='Delete')

class UpdateTaskForm(FlaskForm):
    updatetask = SubmitField()

class SearchTask(FlaskForm):
    search = StringField(validators=validators)
    search_submit = SubmitField(label='Search')

class EditPassword(FlaskForm):
    current_password = PasswordField(label='Current Password', validators=validators)
    new_password = PasswordField(label='New Password', validators=validators)
    confirmation_new_password = PasswordField(label='Confirm New Password', validators=validators)
    save_password = SubmitField()