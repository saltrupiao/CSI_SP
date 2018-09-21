from flask import Flask, render_template, request

# Placeholder for the application
app = Flask(__name__)


# This tells our program the route to our server
@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/calc')
def calc():
    return render_template('calc.html')


# https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['txt']
    new_text = "You entered the word " + text
    return render_template('home.html', new_text = new_text)


if __name__ == '__main__':
    app.run(debug=True) # so the page refreshes live and doesn't need to be restarted
