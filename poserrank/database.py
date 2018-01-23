import sqlite3

# returns a connection to the database
def get_db():
	db = sqlite3.connect('poserrank/db/development.db')
	db.row_factory = sqlite3.Row # this line establishes that we want row objects back from queries, which are useful because they act as dictionaries
	return db
