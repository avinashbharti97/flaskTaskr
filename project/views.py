import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for


#config
app = Flask(__name__)
app.config.from_object('_config')

#functions
def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('you need to login first')
            return redirect(url_for('login'))
    return wrap

#route handlers
def logout():
    session.pop('logged_in', none)
    flash('Goodbye!')
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
    if request.method == 'POST':
        if request.form['username']!= app.config['USERNAME'] or request.form['password']!= app.config['PASSWORD']:
            error = 'Invalid Credential. Please try again'
            return render_template('login.html')
        else:
            session['logged_in'] = True
            flash('Welcome')
            return redirect(url_for('tasks'))
