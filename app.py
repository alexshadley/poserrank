import sqlite3
from flask import Flask
from flask import render_template
app = Flask(__name__)

# returns a connection to the database
def getDB():
	db = sqlite3.connect('db/development.db')
	db.row_factory = sqlite3.Row # this line establishes that we want row objects back from queries, which are useful because they act as dictionaries
	return db

# gets all posers
def getPosers():
	db = getDB()
	result = db.execute('SELECT * FROM posers ORDER BY score DESC;')
	return result

# gets the poser with queryName
def getPoserByName(queryName):
	db = getDB()
	name = (queryName,)
	result = db.execute('SELECT * FROM posers WHERE name=?', name)
	return result

@app.route('/')
def home():
	return render_template('index.html.j2')

@app.route('/top/')
def top():
	posers = getPosers() # connect to the database and retrieve all posers
	return render_template('top.html.j2', posers=posers) # render the 'top' template, with posers as a local variable passed into the template

# this line makes the app run; no idea how
if __name__ == '__main__':
	app.run()
