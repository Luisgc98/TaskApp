from flask import render_template, redirect, url_for, request, flash
from . import do_task
from .forms import ExamenPython1

@do_task.route('/examen1', methods=['GET', 'POST'])
def examen1():
    form_exam = ExamenPython1()
    if request.method == 'POST':
        print(form_exam.ques1.data)

    return render_template('examen1.html', form_exam=form_exam)