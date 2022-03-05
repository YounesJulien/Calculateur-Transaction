from crypt import methods
from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)

db = Database()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html', data=db.getTransactions())

@app.route('/transaction/<id>', methods = ['GET'])
def display(id):
    return render_template('transaction.html', data=db.getTransaction(id))