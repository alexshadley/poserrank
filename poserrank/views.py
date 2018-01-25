from flask import render_template, redirect, url_for, request, session
from poserrank import app
from poserrank.models import User

@app.route('/')
def index():
	return render_template('index.html.j2')

@app.route('/top/')
def top():
	users = User.query.all() # connect to the database and retrieve all posers
	return render_template('top.html.j2', users=users) # render the 'top' template, with posers as a local variable passed into the template

@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html.j2')

	if request.method == 'POST':
		query = User.query.filter(User.username == request.form['username'])
		if query.count() > 0:
			user = query.first()
			if user.password == request.form['password']:
				session['username'] = user.username
				session['authenticated'] = True
				return redirect(url_for('index'))
			else:
				return 'wrong password'

		else:
			return request.form['username'] + ' does not exist'

@app.route('/logout/')
def logout():
	if session['authenticated']:
		session.pop('username', None)
		session['authenticated'] = False
	return redirect(url_for('index'))
