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

@app.route('/transaction/<id>', methods = ['GET', 'POST'])
def display(id):
    return render_template('transaction.html', data=db.getTransaction(id), dis=True)

@app.route('/edit/<id>', methods = ['GET', 'POST'])
def edit(id):
    return render_template('transaction.html', data=db.getTransaction(id), dis=False)

@app.route('/save/<id>', methods = ['GET', 'POST'])
def save(id):
    db.updateTransaction(id, request.form)
    return render_template('home.html', data=db.getTransactions())
