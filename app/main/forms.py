from flask_wtf import FlaskForm         #引入基类
from wtforms import StringField,SubmitField,BooleanField,PasswordField #关于表单HTML标准字段
from wtforms.validators import DataRequired,Email,Length #引入验证函数

class NameForm(FlaskForm): #这是一个名字表单
    name  = StringField('what is your name?',validators=[DataRequired()])
    submit= SubmitField('确定')
