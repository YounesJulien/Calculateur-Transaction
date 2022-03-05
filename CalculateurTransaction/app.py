from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')