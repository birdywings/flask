from . import main
from .forms import NameForm
from .. import db
from ..models import User,Role
from flask import render_template,current_app,redirect,url_for,session
from ..email import send_mail
from datetime import datetime

@main.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['know'] = False
            if current_app.config['FLASKY_ADMIN'] :
                send_mail(current_app.config['FLASKY_ADMIN'],'新用户','mail/new_user',user=user)
        else:
            session['know'] = True

        '''
        old_name=session.get('name')
        if old_name is not None and old_name!=form.name.data :
            flash('你改变了你的名字')
        else :
            flash('你是第一次输入或者你再次输入了同样的名字')
        '''

        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('main.index')) #url_for需要一个内部路由名字作为参数
    return render_template('index.html',current_time=datetime.utcnow()
                           ,form=form,name=session.get('name'),know=session.get('know',False))
