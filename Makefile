run: virtualenv
	bin/python manage.py runserver

setup: virtualenv requirements db

clean:
	rm -rf bin db.sqlite3 include lib pip-selfcheck.json

virtualenv: bin/

bin/:
	virtualenv -p python2 .

requirements:
	bin/pip install -r requirements.txt

db: db.sqlite3

db.sqlite3:
	bin/python manage.py migrate

test:
	bin/python manage.py test tests/

lint:
	bin/pylint whatistheplan

PHONY: setup virtualenv requirements run clean test lint
