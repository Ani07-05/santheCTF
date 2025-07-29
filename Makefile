.PHONY: install run migrate test lint format clean help

help:  ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install dependencies
	poetry install

run:  ## Run the development server
	poetry run python manage.py runserver

migrate:  ## Run database migrations
	poetry run python manage.py migrate

shell:  ## Activate the virtual environment
	poetry shell

test:  ## Run tests
	poetry run pytest

lint:  ## Run linter
	poetry run flake8

format:  ## Format code
	poetry run black .

coverage:  ## Run tests with coverage
	poetry run coverage run -m pytest
	poetry run coverage report

superuser:  ## Create superuser
	poetry run python manage.py createsuperuser

populate:  ## Populate sample challenges
	poetry run python scripts/populate_challenges.py

check:  ## Run Django system checks
	poetry run python manage.py check

collectstatic:  ## Collect static files
	poetry run python manage.py collectstatic --noinput

clean:  ## Clean cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

prod:  ## Run with Gunicorn for production
	poetry run gunicorn santheCTF.wsgi:application

update:  ## Update dependencies
	poetry update

show:  ## Show installed packages
	poetry show
