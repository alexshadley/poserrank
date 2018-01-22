import sqlite3

# returns a connection to the database
def get_db():
	db = sqlite3.connect('poserrank/db/development.db')
	db.row_factory = sqlite3.Row # this line establishes that we want row objects back from queries, which are useful because they act as dictionaries
	return db

# gets all posers
def get_posers():
	db = get_db()
	result = db.execute('SELECT * FROM posers ORDER BY score DESC;')
	return result

# gets the poser with queryName
def get_poser_by_name(queryName):
	db = get_db()
	name = (queryName,)
	result = db.execute('SELECT * FROM posers WHERE name=?;', name)
	return result
