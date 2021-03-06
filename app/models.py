from flask_login import UserMixin, LoginManager
from .data_base import user_data_by_id

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_name):
    return ModelUser.query(id_user=user_name)

class UserDates():
    	def __init__(self, id, user_name, password, init_date, email):
    			self.id = id
			self.user_name = user_name
			self.password = password
			self.init_date = init_date
			self.email = email

class ModelUser(UserMixin):
	def __init__(self, user_dates):
		self.id = user_dates.id
		self.user_name = user_dates.user_name
		self.password = user_dates.password
		self.init_date = user_dates.init_date
		self.email = user_dates.email

	@staticmethod
	def query(id_user):
    		
		user = user_data_by_id(id_user)
		dates = UserDates(
			id=user.id,
			user_name=user.user_name,
			password=user.password,
			init_date=user.init_date,
			email=user.email
		)
		return ModelUser(dates)