from flask import Blueprint, render_template, request, url_for, g
from management.models import Order
from ..forms import OrderForm
from datetime import datetime
from werkzeug.utils import redirect
from .. import db
from management.views.auth_views import login_required


bp = Blueprint('ordered', __name__, url_prefix='/ordered')

@bp.route('/list/')
def _list():
    ordered_list = Order.query.group_by('store_name').order_by(Order.ordered_date.desc())
    return render_template('ordered/ordered_list.html', ordered_list=ordered_list)


@bp.route('detail/<string:ordered_store_name>/')
def detail(ordered_store_name):
    ordered = Order.query.filter_by(store_name=ordered_store_name).all()
    return render_template('ordered/ordered_detail.html', ordered=ordered)

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = OrderForm()
    if request.method == 'POST' and form.validate_on_submit():
        order = Order(store_name=form.store_name.data, order_list=form.order_list.data, ordered_date=datetime.now(), user=g.user)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('ordered/order_form.html', form=form)