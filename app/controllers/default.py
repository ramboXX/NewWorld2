from app import app
from flask import render_template

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/cadastre.html')
def cadastre():
    return render_template('cadastre.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/sobre.html')
def sobre():
    return render_template('sobre.html')