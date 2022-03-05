import sqlite3
from unittest import result

class Database():
  
  def __init__(self):
    self.connection = None

  def get_connection(self):
    if self.connection is None:
      self.connection = sqlite3.connect("db/database.db")
    return self.connection
  
  def disconnect(self):
    if self.connection is not None:
      self.connection.close()
      self.connection = None

  def execute(self, query):
    connection = self.get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    self.disconnect()
    return result

  def update(self, query):
    connection = self.get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    self.disconnect()

  def getTransactions(self):
    return self.execute("SELECT * FROM Trans ORDER BY TransDate DESC")

  def getTransaction(self, id):
    return self.execute("SELECT * FROM Trans WHERE id=" + id)[0]

  def updateTransaction(self, id, form):
    self.update("UPDATE Trans SET TransDate='" 
      + form['date'] + "', PlaceName='" + form['place'] + "', Amount=" 
      + form['amount']+  " WHERE id=" + id)