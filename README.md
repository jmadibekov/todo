# Todo List Manager

This is a small mini webapp that uses following tools (not an exhaustive list):
- Django & DRF (for the webapp with RESTful API)
- Docker Compose (to isolate multiple stacks)
- Redis (for caching)
- PostgreSQL (for database)

The app is ready for production.

## Getting Started

To build and run the app, clone the repo and use the following command after installing Docker:

```bash
docker-compose up
```

Once it has started, you can open your browser to [http://localhost:8000/api](http://localhost:8000/api).
- You can also head to [http://localhost:8000/admin](http://localhost:8000/admin), but you need to first create superuser for that.

## Environment
Environment `.env` file is included in GitHub for convenience purposes with development variables. Make sure to change the
variables to secret production variables when you deploy.

## Testing

The project contains basic tests to check models & API. Run the following command from web container at the Docker to test:
```bash
python manage.py test
```

## Dependency Management

Dependencies are managed via [Poetry](https://python-poetry.org). Run the following [command](https://python-poetry.org/docs/cli/) to export the lock file to requirements.txt file:
```bash
poetry export -f requirements.txt --output requirements.txt
```
