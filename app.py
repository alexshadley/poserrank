import sqlite3
from flask import Flask
from flask import render_template
app = Flask(__name__)

# returns a connection to the database
def getDB():
	db = sqlite3.connect('db/dev.db')
	return db

@app.route('/')
def home():
	return render_template('index.html.j2')

@app.route('/top/')
def top():
	return render_template('top.html.j2')

# this line makes the app run; no idea how
if __name__ == '__main__':
	app.run()
