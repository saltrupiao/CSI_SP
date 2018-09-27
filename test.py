from flask import Flask, render_template, request

# Placeholder for the application
app = Flask(__name__)


# This tells our program the route to our server
@app.route('/')
def home1():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


# https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
@app.route('/', methods=['POST'])
def my_form_post():
    int1 = (request.form['num1'])
    int2 = (request.form['num2'])
    operation = (request.form['op'])
    result = compute(operation, int(int1), int(int2))

    if result != 'null':
        new_text = "The Total is " + str(result)
        return render_template('home.html', new_text=new_text)
    else:
        new_text = "There was an error. Please try again."
        return render_template('home.html', new_text=new_text)


def compute(x, y, z):
    if x == '+':
        return add(y, z)
    elif x == '-':
        return subtract(y, z)
    elif x == '*':
        return multiply(y, z)
    elif x == '/':
        return divide(y,z)
    else:
        return 'null'


def add(x, y):  # add two integers
    return x + y


def multiply(x, y):  # multiply two integers
    return x * y


def subtract(x, y):  # subtract two integers
    return x - y


def divide(x, y):  # integer divide two integers
    return x/y


if __name__ == '__main__':
    app.run(debug=True) # so the page refreshes live and doesn't need to be restarted
