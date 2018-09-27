from flask import Flask, render_template, request


def calc():
    input = (request.form['calculate'])
    output = eval(input)
    result = "= " + str(output)
    return render_template('calc.html', new_text=result)

# int1 = (request.form['num1'])
# int2 = (request.form['num2'])
# operation = (request.form['op'])
# result = compute(operation, int(int1), int(int2))


# def compute(x, y, z):
#     if x == '+':
#         return add(y, z)
#     elif x == '-':
#         return subtract(y, z)
#     elif x == '*':
#         return multiply(y, z)
#     elif x == '/':
#         return divide(y,z)
#     else:
#         return 'null'
#
#
# def add(x, y):  # add two integers
#     return x + y
#
#
# def multiply(x, y):  # multiply two integers
#     return x * y
#
#
# def subtract(x, y):  # subtract two integers
#     return x - y
#
#
# def divide(x, y):  # integer divide two integers
#     return x/y


