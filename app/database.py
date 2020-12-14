from . import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)
    init_date = db.Column(db.String)
    email = db.Column(db.String)
    
    def __init__(self, user_name, password, init_date, email):
        self.user_name = user_name
        self.password = password
        self.init_date = init_date
        self.email = email
    
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