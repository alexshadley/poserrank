from poserrank import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique=True)
	full_name = db.Column(db.String(64))
	email = db.Column(db.String(64), unique=True)
	password = db.Column(db.String(64))
	score = db.Column(db.Integer)

	def __repr__(self):
		return '<User %r' % self.username

"""
# Drunk Alex welcomes you to his work
class Users:
	def get_users():
		conn = db.get_db() # get a database connection
		result = conn.execute('SELECT * FROM users ORDER BY score DESC;') # use the connection to retrieve all users
		users = [] # ELO is so great
		for row in result:
			users.append(User(result.fetchone()))
		return users

	# gets the user with queryName
	def get_user_by_name(queryName):
		db = db.get_db()
		name = (queryName,)
		result = db.execute('SELECT * FROM posers WHERE name=?;', name)
		return User(result.fetchone())

	def add_user(paramDict):
		newUser = User(paramDict)
		conn = db.get_db()
		db.execute('INSERT INTO users (?, ?, ?);', )

class User:
	def __init__(self, row):
		self.name = row['name']
		self.email = row['email']
		self.score = row['score']
"""
