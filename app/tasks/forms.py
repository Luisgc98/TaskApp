from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, TextField, SubmitField
from wtforms.fields.core import RadioField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
from datetime import datetime as current_date

validators = [DataRequired()]

class ExamenPython1(FlaskForm):
    ques1 = TextAreaField('¿Qué es Python?')
    ques2 = TextAreaField('Menciona tres palabras reservadas del lenguaje de programación Python.')
    ques3 = TextAreaField('Declara los tipos de variables que hay en Python:')
    ques4 = TextAreaField('¿Qué es una lista en Python?')
    ques5 = TextAreaField('¿Qué es un diccinario en Python?')
    ques6 = TextAreaField('¿Cuál es la diferencia entre una lista y una tupla?')
    ques7 = TextAreaField('Escribe las diferentes maneras de agregar variables dentro de una cadena de texto:')
    ques8 = TextAreaField('¿Una cadena de texto funciona igual que una lista con caracteres? Escribe tu explicación.')
    ques9 = TextAreaField('Si escribo la frase: "El día de hoy hago examen", en python ¿cómo sabría cuántas palabras ingrese?')
    #ques10 = RadioField(label='Si x="123.4"\n¿Cuál de las siguientes opciones marcaría error?', choices=[('y=list(x)', 'y = list(x)'), ('z=int(x)', 'z = int(x)')])
    ques11 = TextAreaField('Teniendo la palabra "Hola Mundo" en un bucle for de la siguiente manera: \n\nfor i in "Hola Mundo":\n\tprint(i, ________)\n\nEscribe la palabra reserva que hace falta en la línea para que imprima todo en la misma línea.')
    submit = SubmitField('Enviar Respuestas')