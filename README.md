# SantheCTF

A Django-based Capture The Flag (CTF) platform for hosting cybersecurity challenges.

## Features

- User registration and authentication
- Challenge management system
- Leaderboard and scoring
- Various cipher challenges (Caesar, Atbash, ROT13, Base64, etc.)
- Admin interface for challenge management

## Getting Started

### Prerequisites

- Python 3.11+
- Poetry (for dependency management)

### Installation

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the repository** (if needed):
   ```bash
   git clone <repository-url>
   cd santhectf
   ```

3. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

4. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

5. **Run database migrations**:
   ```bash
   poetry run python manage.py migrate
   ```

6. **Populate challenges** (optional):
   ```bash
   poetry run python scripts/populate_challenges.py
   ```

7. **Create a superuser** (optional):
   ```bash
   poetry run python manage.py createsuperuser
   ```

8. **Run the development server**:
   ```bash
   poetry run python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

### Quick Start Commands

After installation, you can use these commands:

```bash
# Run the development server
poetry run python manage.py runserver

# Run migrations
poetry run python manage.py migrate

# Create superuser
poetry run python manage.py createsuperuser

# Populate sample challenges
poetry run python scripts/populate_challenges.py
```

### Using Make Commands (Optional)

For convenience, you can also use the provided Makefile:

```bash
# See all available commands
make help

# Install dependencies
make install

# Run the development server
make run

# Run migrations
make migrate

# Create superuser
make superuser

# Populate challenges
make populate

# Run tests
make test

# Format code
make format

# Run linter
make lint
```

## Development

### Managing Dependencies

Add a new dependency:
```bash
poetry add package-name
```

Add a development dependency:
```bash
poetry add --group dev package-name
```

Update dependencies:
```bash
poetry update
```

Show installed packages:
```bash
poetry show
```

### Code Formatting

This project uses Black for code formatting:

```bash
poetry run black .
```

### Linting

Run flake8 for linting:

```bash
poetry run flake8
```

### Testing

Run tests with pytest:

```bash
poetry run pytest
```

With coverage:

```bash
poetry run coverage run -m pytest
poetry run coverage report
```

## Production Deployment

For production deployment with Gunicorn:

```bash
poetry run gunicorn santheCTF.wsgi:application
```

## Project Structure

```
santhectf/
├── ctf/                    # Main CTF application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── urls.py            # URL patterns
│   └── templates/         # HTML templates
├── santheCTF/             # Django project settings
├── scripts/               # Utility scripts
├── static/                # Static files
├── manage.py              # Django management script
└── pyproject.toml         # Poetry configuration
```

## License

[Add your license information here]
