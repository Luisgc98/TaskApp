from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://webadmin:KIYntc67386@node50361-taskappmanager.in1.cloudjiffy.net:11097/book1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Unicode)
    password = db.Column(db.Unicode)
    init_date = db.Column(db.Unicode)

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.init_date = str(datetime.datetime.now().date())