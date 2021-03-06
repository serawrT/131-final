from crypt import methods
from trace import Trace
from turtle import back
from unicodedata import category
import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "mydatabase.db")
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Expense(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    expensename = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)


@budget.route('/')
def add():
    return render_template("add.html")


@budget.route("/expenses")
def expenses():
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)


@budget.route('/addexpense', methods=["POST"])
def addexpense():
    date = request.form["date"]
    expensename = request.form['expensename']
    amount = request.form["amount"]
    category = request.form["category"]
    print(date + " " + expensename + " " + amount + " " + category)
    expense = Expense(date=date, expensename=expensename,
                      amount=amount, category=category)

    db.session.add(expense)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":

    app.run(debug=True)
