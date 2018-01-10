import sqlite3

def generateDB():
	db = sqlite3.connect('db/development.db')
	db.execute('CREATE TABLE posers (ranking integer, name text, score integer);')

if __name__ == '__main__':
	generateDB()
