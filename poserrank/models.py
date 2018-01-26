from poserrank import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique=True)
	full_name = db.Column(db.String(64))
	email = db.Column(db.String(64), unique=True)
	password = db.Column(db.String(64))
	score = db.Column(db.Integer, default=0)

	def __repr__(self):
		return '<User %r' % self.username
