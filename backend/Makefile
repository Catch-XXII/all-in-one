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