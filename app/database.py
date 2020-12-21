from sqlalchemy.sql.schema import ForeignKey
from . import SQLAlchemy

db = SQLAlchemy()

#---------------------------------------------------------
# Clase de los Usuarios.
class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    area = db.Column(db.String)
    init_date = db.Column(db.Date)
    role = db.Column(db.String)
    
    def __init__(self, user_name, password, init_date, email, area):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.init_date = init_date
        self.area = area
        self.role = 'DEFAULT'
    
    @staticmethod
    def all_users():
        return users.query.all()

    @staticmethod
    def user_by_id(id):
        user = users.query.filter_by(id=id).first()
        return user
    
    @staticmethod
    def user_by_username(username):
        user = users.query.filter_by(user_name=username).first()
        return user

    @staticmethod
    def user_by_email(email):
        user = users.query.filter_by(email=email).first()
        return user

    @staticmethod
    def add_user(new_user):
        try:
            db.session.add(new_user)
            db.session.commit()
            return f'Felicitaciones! Usuario {new_user.user_name} con el correo {new_user.email} registrado con éxito.'
        except:
            db.session.rollback()
            return 'Fallo en el registro. Inténtelo de nuevo más tarde.'

#---------------------------------------------------------
# Clase de la tareas.
class tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String)
    description = db.Column(db.String)
    group_id = db.Column(db.String)
    publication_date = db.Column(db.Date)
    delivery_date = db.Column(db.Date)
    user_publishes = db.Column(db.String)

    def __init__(self, task_name, description, group_id, publication_date, delivery_date, user_publishes):
        self.task_name = task_name
        self.description = description
        self.group_id = group_id
        self.publication_date = publication_date
        self.delivery_date = delivery_date
        self.user_publishes = user_publishes

    @staticmethod
    def get_all_tasks():
        return tasks.query.all()

#------------------------------------------
# Clase de las tareas de los usuarios.
class tasks_users(db.Model):
    __tablename__ = 'tasks_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(users.id))
    task_id = db.Column(db.Integer, db.ForeignKey(tasks.id))
    status = db.Column(db.String)
    qualification = db.Column(db.String)
    delivery_date = db.Column(db.Date)

    def __init__(self, user_id, task_id, status, qualification, delivery_date):
        self.user_id = user_id
        self.task_id = task_id
        self.status = status
        self.qualification = qualification
        self.delivery_date = delivery_date