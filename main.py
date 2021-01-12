
from flask import Flask, render_template, jsonify, request
#from test import get_price

app = Flask(__name__)


#@app.route('/', methods=["POST"])
@app.route('/')
def home():
    """if request.method == 'POST':
        form = request.form
        selection = form["symbol"]
        price=get_price(selection)
    else:
        price="""""
    price=""
    return render_template("home.html", price=price)


@app.route('/stocks/')
def stocks():
    return render_template("stocks.html")


@app.route('/signup/')
def signup():
    return render_template("signup.html")


@app.route('/login/')
def login():
    return render_template("login.html")





if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')