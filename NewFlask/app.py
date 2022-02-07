from flask import Flask, render_template, request, flash
from datetime import date

app = Flask(__name__)
app.secret_key = "1f07j3109jf571fn"


@app.route('/')
@app.route('/home')
def index():
    flash("What is your name?")
    return render_template('base.html')

@app.route("/hello", methods=['POST', 'GET'])
def hello():
    flash("Hello, " + str(request.form['input']))
    return render_template("base.html")

@app.route("/thedate", methods=['POST', 'GET'])
def whattime():
    flash("The date is " + str(date.today()))
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)