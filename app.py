from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,World!'

@app.route('/<name>')
def hello(name):
    return f'<h1>Hello, {name}!<h1>'

@app.route('/double/<number>')
def double(number):
    return 2*int(number)
