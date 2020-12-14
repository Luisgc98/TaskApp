from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, TextField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

validators = [DataRequired()]
class LoginForm(FlaskForm):
    user_name = StringField('Correo o nombre de usuario', validators=validators)
    password = PasswordField('Contraseña', validators=validators)
    login_submit = SubmitField('Ingresar')
    
class SignUpForm(FlaskForm):
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    names = StringField('Nombre(s)', validators=validators)
    surnames = StringField('Apellidos', validators=validators)
    area = StringField('Área', validators=validators)
    new_password = PasswordField('Nueva contraseña', validators=validators)
    password_confirmation = PasswordField('Confirmar contraseña', validators=validators)
    signup_submit = SubmitField('Registrar')