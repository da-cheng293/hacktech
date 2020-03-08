#from flask import Flask, render_template
# 
# app = Flask(__name__)
# 
# 
# @app.route('/')
# def index():
#     return render_template('login.html')
# 
# 
# @app.route('/')
# def index():
#     return render_template('login.html')
# 
# 
# @app.route('/')
# def index():
#     return render_template('login.html')
# 
# 
# @app.route('/')
# def index():
#     return render_template('login.html')
# 
# 
# @app.route('/')
# def index():
#     return render_template('login.html')
# 
# 
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, copy_current_request_context
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, TextField
from passlib.hash import sha256_crypt
from functools import wraps
import datetime
from flask import Flask, request, url_for
#from flask_mail import Mail, Message
#import smtplib
#from email.mime.text import MIMEText
#from email.header import Header
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
#import smtplib, yagmail
#from random_words import RandomWords
#from apscheduler.schedulers.background import BackgroundScheduler
#from _thread import start_new_thread
import  time
from wtforms.widgets import Select, TextInput
import pandas as pd
from werkzeug.utils import secure_filename
from pandas.io import sql
import pymysql
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR

from sqlalchemy.types import BigInteger


app = Flask(__name__)
app.secret_key = 'Temp1234'

# Config MySQL


s = URLSafeTimedSerializer('Temp1234')





# Check if user logged in



@app.route('/', methods=['GET', 'POST'])

def slide():
    return render_template('slide.html')


@app.route('/correct', methods=['GET', 'POST'])

def correct():
    return render_template('correct.html')

@app.route('/wrong_explain', methods=['GET', 'POST'])

def wrong_explain():
    return render_template('wrong_explain.html')

@app.route('/search_and_display', methods=['GET', 'POST'])

def search_and_display():
    return render_template('search_and_display.html')


@app.route('/search_content', methods=['GET', 'POST'])

def search_content():
    return

@app.route('/upload_file', methods=['GET', 'POST'])

def upload_file():
    return


if __name__ == '__main__':

   app.run(debug=True)
  # app.run(debug=True, host='147.128.12.217', port=8080)
