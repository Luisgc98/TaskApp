from flask import Blueprint

record = Blueprint('record', __name__, url_prefix='/record')

from . import views