.PHONY: dev-run start-redis stop-redis lint test

dev-run:
	python run.py

start-redis:
	brew services start redis

stop-redis:
	brew services stop redis

lint:
	ruff check . --fix

test:
	pytest tests/

setup:
	./setup.py setup

dev:
	./setup.py dev

prod:
	./setup.py prod

start:
	./setup.py start

start-dev:
	./setup.py start:dev

start-prod:
	./setup.py start:prod