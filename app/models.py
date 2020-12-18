from flask_login import UserMixin, LoginManager
from .database import users
from . import login_manager

class UserDates():
	def __init__(self, id, user_name, password, email, init_date, area, role):
		self.id = id
		self.user_name = user_name
		self.password = password
		self.email = email
		self.init_date = init_date
		self.area = area
		self.role = role

class ModelUser(UserMixin):
	def __init__(self, user_dates):
		self.id = user_dates.id
		self.user_name = user_dates.user_name
		self.password = user_dates.password
		self.email = user_dates.email
		self.init_date = user_dates.init_date
		self.area = user_dates.area
		self.role = user_dates.role

	@staticmethod
	def query(id):
		user = users.user_by_id(id=id)
		dates = UserDates(
			id=user.id,
			user_name=user.user_name,
			password=user.password,
			email=user.email,
			init_date=user.init_date,
			area=user.area,
			role=user.role
		)
		return ModelUser(dates)

@login_manager.user_loader
def load_user(id):
    return ModelUser.query(id=id)