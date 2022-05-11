import random

from Auth import app
from Auth.forms import RegisterForm, LoginForm
from Auth.models import User
from flask import render_template, flash, redirect, url_for, request


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/login')
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=(['GET', 'POST']))
def register_page():

    form = RegisterForm()
    if request.method == 'POST':
        print("working")

    if form.validate_on_submit():
        return redirect(url_for('login_page'))

    return render_template('register.html', form=form)
