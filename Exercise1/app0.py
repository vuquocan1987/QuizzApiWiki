from flask import Flask
app = Flask("hello")

@app.route("/")
def index(name):
    return "We have plus,minus and multiply function, all the functions you want in the world"

@app.route("/add/<float:number_1>/<float:number_2>/")
def add(number_1, number_2):
    return f"{number_1 + number_2}"

@app.route("/sub/<float:number_1>/<float:number_2>/")
def sub(number_1, number_2):
    return f"{number_1 - number_2}"
@app.route("/mul/<float:number_1>/<float:number_2>/")
def mul(number_1, number_2):
    return f"{number_1 * number_2}"

@app.route("/div/<float:number_1>/<float:number_2>/")
def div(number_1, number_2):
    return f"{number_1 / number_2}" if number_2 != 0 else "NaN"
