from crypt import methods
from trace import Trace
from turtle import back
from flask import Flask, render_template, request

app = Flask(__name__)


@back_end.route('/')
def add():
    return render_template("add.html")


@back_end.route('/addexpense', methods=["POST"])
def addexpense():
    date = request.form["date"]
    expensename = request.form['expensename']
    amount = request.form["amount"]
    catagory = request.form["category"]
    print(date + " " + expensename + " "amount + " " + category)
    return redirect(("/"))


if __name__ == '__main__':  # coomenting

    app.run(debug=True)
