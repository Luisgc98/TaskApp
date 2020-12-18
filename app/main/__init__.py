from flask import Blueprint
main = Blueprint('main', __name__, url_prefix='/auth')

from . import views