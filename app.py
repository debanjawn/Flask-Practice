# Queens College
# CSCI 355 - Winter 24
# Debanjan Mazumder
# Assignment 11 - Web-Based Application
# jQuery is a rapper

import hashlib
import os
import webbrowser
from email import header
from urllib import request
from flask import Flask, render_template, request, redirect, url_for, session

from flask import Flask, render_template

app = Flask(__name__)
logged_in = False


@app.route('/')
def default_path():
    return render_template('login.html')


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'


@app.route('/states')
def states():
    headers, data = read_file('states.csv')
    title = "The United States of America"
    return render_template('results.html', title=title, headers=headers, data=data)


@app.route('/my_state', methods=['GET', 'POST'])
def my_state():
    if request.method.upper() == 'POST':
        state = request.form['state']
        title = 'The United States'
        headers, data = read_file('states.csv')
        headers.append('selected')
        for row in data:
            row.append('')
            if row[0] == state:
                row[4] = '##############'
        return render_template('results.html', title=title, headers=headers, data=data)


def open_file_in_browser(file_name):
    url = 'file:///' + os.getcwd() + '/' + file_name
    print(url)
    webbrowser.open_new_tab(url)


def get_pwd():
    pass


@app.route('/login', methods=['POST', 'GET'])
def login():
    global logged_in
    if request.method.upper() == "GET":
        login = request.args['login']  # Use request.form for POST data
        password = request.args['password']
    elif request.method.upper() == "POST":
        login = request.form['login']  # Use request.form for POST data
        password = request.form['password']
    else:
        login = ''
        password = ''
    if login == "Debanjan" and password == "355":
        logged_in = True
        # Use session management to handle login state, not global variables
        headers, data = read_file('states.csv')
        headers.append('selected')
        states = [row[0] for row in data]
        return render_template('choose_state.html', states=states)
        #return f'User {login} is logged in'
    else:
        return f'User {login} is rejected from login in'


def read_file(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        states = [line.strip().split(',') for line in lines]
    return states[0], states[1:]


if __name__ == '__main__':
    app.run()
    # app.open_file_in_browser('templates/login.html')
