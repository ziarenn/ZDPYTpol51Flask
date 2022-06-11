from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    name = request.form['name']
    age = request.form['age']
    rate = request.form['score']
    return render_template('score.html', name=name, age=age, rate=rate)