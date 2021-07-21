from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

class OrderForm(FlaskForm):
    store_name = StringField('가게명', validators=[DataRequired()])
    order_list = TextAreaField('주문 내용', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    phone_number = StringField('휴대폰 번호', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])