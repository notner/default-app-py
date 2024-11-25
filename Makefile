default: help

dev-setup:
	@python3 -m venv .virtualenv/
	@pip install -r requirements/prod.in
	@pip install -r requirements/dev.in
	@pip install -e .

start-fixtures:
	cd docker && docker-compose up

stop-fixtures:
	cd docker && docker-compose down --volumes

run-web:
	@.virtualenv/bin/python src/defaultapp/web/server.py

check-code:
	@.virtualenv/bin/flake8 --ignore=W191,E501 src/
	# @.virtualenv/bin/mypy src/

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rfv ./src/default_app.egg-info


run-tests:
	export PYTHONDONTWRITEBYTECODE=1
	@.virtualenv/bin/pytest


help:
	echo 'help needed?'

	echo 'dev-setup'
	echo 'run-fixtures'
	echo 'run-tests'
	echo 'pip-compile'
	echo 'install-local version'
	echo 'install-prod version'
