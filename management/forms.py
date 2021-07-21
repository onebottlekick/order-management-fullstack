from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    store_name = StringField('가게명', validators=[DataRequired()])
    order_list = TextAreaField('주문 내용', validators=[DataRequired()])
