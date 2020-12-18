from . import SQLAlchemy

db = SQLAlchemy()

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