run: virtualenv
	bin/python manage.py runserver

setup: virtualenv requirements db

clean:
	rm -rf bin db.sqlite3 include lib pip-selfcheck.json

virtualenv: bin/

bin/:
	virtualenv -p python2 .

requirements: lib/python2.7/site-packages/django

lib/python2.7/site-packages/django:
	bin/pip install -r requirements.txt

db: db.sqlite3

db.sqlite3:
	bin/python manage.py migrate

PHONY: setup virtualenv requirements run clean
