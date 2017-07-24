from flask import Blueprint

main = Blueprint('main',__name__) #登记main蓝本

from . import errors,views

