# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:04:03 2024

@author: user
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello Flask</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,{}!</h1>'.format(name)

@app.route('/user/<name>/<surname>')
def user(name,surname):
    return '<h1>Hello,{}{}<!/h1>'.format(name,surname)

if __name__ == '__main__':
    app.run()