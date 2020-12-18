from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, TextField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
from werkzeug.security import check_password_hash, generate_password_hash
from .database import users
from .mail_senders import mail_sender_wel
from datetime import datetime as current_date

validators = [DataRequired()]
class LoginForm(FlaskForm):
    user_name = StringField('Correo o Nombre de Usuario', validators=validators)
    password = PasswordField('Contraseña', validators=validators)
    login_submit = SubmitField('Ingresar')

    def validate_passwd(self, pwhash):
        password = self.password.data
        if check_password_hash(pwhash=pwhash, password=password):
            return True
        else: return False

    def validate_user(self):
        user_log = self.user_name.data
        user = users.user_by_username(username=user_log)
        login_by_username = False
        if user: login_by_username = True
            
        if login_by_username:
            log = self.validate_passwd(pwhash=user.password)
            if log: return user
            else: return False
        else:
            user = users.user_by_email(email=user_log)
            if user:
                log = self.validate_passwd(pwhash=user.password)
                if log: return user
                else: return False
            else: 
                return None

    def validate_role(self, user):
        role = user.role
        if role != 'DEFAULT':
            return True
        else:
            return False
    
class SignUpForm(FlaskForm):
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    names = StringField('Nombre(s)', validators=validators)
    surnames = StringField('Apellidos', validators=validators)
    area = SelectField('Área', validators=validators, choices=[
                                                                ('', '--Seleccionar área--'), 
                                                                ('sinesis', 'SINESIS'), 
                                                                ('dev', 'DEV'), 
                                                                ('space', 'SPACE'), 
                                                                ('aov', 'AOV'), ])
    new_password = PasswordField('Nueva contraseña', validators=validators)
    password_confirmation = PasswordField('Confirmar contraseña', validators=validators)
    signup_submit = SubmitField('Registrar')

    def validate_signup(self, list_users):
        email = self.email.data.strip()
        exist = False
        for user in list_users:
            if email == user.email: 
                exist = True
        if exist:
            return False
        else:
            password = self.new_password.data.strip()
            passwd_db = generate_password_hash(password)
            user_name = self.names.data.strip()+' '+self.surnames.data.strip()
            area = self.area.data.strip()
            init_date = current_date.now().date()
            new_user = users(
                user_name=user_name,
                password=passwd_db,
                email=email,
                area=area,
                init_date=init_date
            )
            return new_user

    def add_user(self, new_user):
        return users.add_user(new_user=new_user)

    def send_mail(self, email, user_name, password):
        return mail_sender_wel(email=email, user_name=user_name, password=password)