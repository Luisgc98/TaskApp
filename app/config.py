class Config:
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://luisgc:Sk81398@localhost/example'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'luis.gurrola.condor@gmail.com'
    MAIL_PASSWORD = 'zpeynmzgyyhkmbtx'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True