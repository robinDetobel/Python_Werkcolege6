from flask import Flask
from flask import request
from flask import render_template
import random as rd
app = Flask(__name__)


#voorbeelden begin
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<user>')
def hello_user(user):
    return "hello %s" %user

@app.route('/sum', methods=['POST'])
def sum():
    a = int(request.values['A'])
    b = int(request.values['B'])
    sub = a + b
    return str(sub)

@app.route('/me')
def json_name():
    return{
        "first name": "Robin",
        "last name": "Detobel"
    }

@app.route('/index/<name>',methods=['GET', 'POST'])
def show_html(name):
    return render_template('index.html', name = name)

#voorbeelden end

#opdracht 1
@app.route('/lucky')
def luckynr():
    nr = rd.randint(1,10)
    return str(nr)


#opdracht 2
@app.route('/power/<number>', methods=['POST'])
def power(number):
    x = int(number)
    power_getal = x * x
    return str(power_getal)

#opdracht 3
@app.route('/event')
def event():
    return{
        "id": "1",
        "naam":"Graspop",
        "locatie": "Belgie"
    }

if __name__ == '__main__':
    app.run()
