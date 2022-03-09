from contextlib import nullcontext
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
    return render_template('transaction.html', data=db.getTransaction(id), Options=db.getPlaceNames(), dis=True)

@app.route('/edit/<id>', methods = ['POST'])
def edit(id):
    return render_template('transaction.html', data=db.getTransaction(id), Options=db.getPlaceNames(), dis=False)

@app.route('/save/<id>', methods = ['POST'])
def save(id):
    if int(id,base=10) == db.getNewId():
        db.newTransaction(id, request.form)
    else:
        db.updateTransaction(id, request.form)
    return render_template('transaction.html', data=db.getTransaction(id), Options=db.getPlaceNames(), dis=True)

@app.route('/new', methods = ['GET'])
def new():
    return render_template('transaction.html', data=[db.getNewId(), '', 0], Options=db.getPlaceNames(), dis=False)