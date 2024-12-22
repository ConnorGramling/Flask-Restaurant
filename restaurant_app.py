from flask import Flask, render_template, request, redirect, url_for, abort
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from order_model import Base, Order

app = Flask(__name__)

engine = create_engine("sqlite:///orders.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
def default():
    return redirect(url_for("main_menu", table_number=1))

@app.route("/table/<int:table_number>")
def main_menu(table_number):
    return render_template(
        "main_menu.html", 
        table_number=table_number, 
        order_summary_ref=url_for("order_summary", table_number=table_number)
    )

@app.route("/order_summary/<int:table_number>", methods=["POST"])
def order_summary(table_number):
    customer_name = request.form["customer_name"]
    order_items = request.form["order_summary"]
    
    order_dict = {
        "customer_name": customer_name,
        "order_items": order_items.split(", "),
        "table_number": table_number
    }

    new_order = Order(customer_name=customer_name, order_items=order_items.split(
        ", "), table_number=table_number)
    try:
        new_order = Order(
            customer_name=customer_name,
            order_items=order_items,
            table_number=table_number
        )
        session.add(new_order)
        session.commit()
        return render_template("order_summary.html", order=order_dict)
    except Exception as e:
        print(e)
        return "Error placing order"

@app.route("/kitchen/")
def kitchen():
    orders = session.query(Order).all()
    orders_json = [order.toJSON() for order in orders]
    return render_template("kitchen.html", orders=orders_json)


@app.route("/delete/<int:order_id>")
def delete_order(order_id):
    order_to_delete = session.query(Order).get(order_id)
    if order_to_delete is None:
        abort(404)
    try:
        session.delete(order_to_delete)
        session.commit()
        return redirect(url_for("kitchen"))
    except Exception as e:
        print(e)
        return "Error deleting order"


if __name__ == "__main__":
    app.run(debug=True)
