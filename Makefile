VERBOSITY ?= 1

run: virtualenv
	bin/python manage.py runserver

setup: virtualenv requirements db

clean:
	rm -rf bin db.sqlite3 include lib pip-selfcheck.json ./**/*.pyc ./**/__pycache__/

virtualenv: bin/

bin/:
	virtualenv -p python2 .

requirements:
	bin/pip install -r requirements.txt

db:
	bin/python manage.py migrate

test:
	bin/python manage.py test -v $(VERBOSITY) tests/

lint:
	bin/pylint whatistheplan

coverage:
	bin/coverage run --source=whatistheplan manage.py test tests/
	bin/coverage html

PHONY: setup virtualenv requirements run clean test lint
