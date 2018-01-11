# PoserRank

A revolutionary website that allows users to stay up to date with the leading
posers globally, as well as report acts of posery.

# Dependencies

1. Flask - http://flask.pocoo.org/
2. Sqlite - https://www.sqlite.org/

# Submodules

This project makes use of git submodules to organize its Bulma dependencies.
Submodules are a means of including repository (Bulma) inside another
repo (PoserRank).  Read more about submodules
[here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

It is important to note that whenever cloning a repo containing submodules, the
submodules are not immediately retrieved, but rather this must be done manually.
To do this, run the following commands in the base directory:

```
git submodule init
```

```
git submodule update
```

# Installation and Use

1. Clone the repository to a local repository of choice.
2. Retrieve the Bulma repo at https://github.com/jgthms/bulma (see above instructions)
3. Execute generate_db.py with python to generate the development database.
4. Run app.py with python.
5. Open the index page on a web browser (localhost:5000 by default).

# Useful Links

* Python Sqlite3 Documentation - https://docs.python.org/3/library/sqlite3.html
* Bulma Documentation - https://bulma.io/documentation/overview/start/
* Using sass with Flask - https://stackoverflow.com/questions/14412677/using-sass-with-flask-and-jinja2
