from management import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(200), nullable=False)
    order_list = db.Column(db.Text(), nullable=False)
    ordered_date = db.Column(db.DateTime(), nullable=False)