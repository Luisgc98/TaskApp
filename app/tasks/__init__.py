from flask import Blueprint
do_task = Blueprint('do_task', __name__, url_prefix='/do_task')

from . import views