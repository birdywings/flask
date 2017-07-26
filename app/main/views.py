from . import main
from .forms import NameForm
from .. import db
from ..models import User,Role
from flask import render_template,current_app,redirect,url_for,session
from ..email import send_mail
from datetime import datetime

@main.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())
