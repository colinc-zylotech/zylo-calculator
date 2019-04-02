.PHONY: test

all: install test run-dev

install:
	pip install pipenv
	pipenv install --dev

install-prod:
	pip install pipenv
	pipenv install

test: format lint
	$(shell pipenv --venv)/bin/pytest -v

lint:
	$(shell pipenv --venv)/bin/pylint -v -f colorized core tests web_app

format:
	$(shell pipenv --venv)/bin/black -v core tests web_app

run-dev:
	FLASK_ENV=development FLASK_APP=web_app/app.py $(shell pipenv --venv)/bin/flask run --host 0.0.0.0

run-prod:
	$(shell pipenv --venv)/bin/gunicorn web_app.app:APP -b 0.0.0.0:8000

run-docker-dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build

run-docker-prod:
	docker-compose up --build
