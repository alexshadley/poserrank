import sqlite3

def generate_db():
	db = sqlite3.connect('development.db')
	db.execute('CREATE TABLE users (name text, email text, score integer);')

if __name__ == '__main__':
	generate_db()
