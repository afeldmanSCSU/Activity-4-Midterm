from flask import Flask

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add_nums(num1, num2):
  sum = num1 + num2
  return str(sum)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract_nums(num1, num2):
  sum = num1 - num2
  return str(sum)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply_nums(num1, num2):
  sum = num1 * num2
  return str(sum)

@app.route('/divide/<int:num1>/<int:num2>')
def divide_nums(num1, num2):
  sum = num1 / num2
  return str(sum)
