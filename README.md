# Todo List Manager

This is a small mini webapp that uses following tools (not an exhaustive list):
- Django & DRF (for the webapp with RESTful API)
- Docker Compose (to isolate multiple stacks)
- Redis (for caching)
- PostgreSQL (for database)

The app is ready for production.

## Getting Started

To build and run the app in the development mode, clone the repo and use the following command after installing Docker:

```bash
docker-compose up --build
```

Once it has started, you can open your browser to [http://localhost:8000/api](http://localhost:8000/api).
- You can also head to [http://localhost:8000/admin](http://localhost:8000/admin), but you need to first create superuser for that.

Note that you might be asked to give permission to run `entrypoint.sh` file in the container, fix that with the command:
```bash
chmod +x ./entrypoint.sh
```

## Production
The app is ready to be deployed to production. All you need is to include the secret production
environment files `.env.prod` and `.env.prod.db` at the root directory and run the following
command at the server:

```bash
docker-compose up -f docker-compose.prod.yaml up --build
```

Note that you might be asked to give permission to run `entrypoint.prod.sh` file in the container, fix that with the command:
```bash
chmod +x ./entrypoint.prod.sh
```

## Testing

The project contains basic tests to check models & API. Run the following command from web container at the Docker to test:
```bash
python manage.py test
```

## Dependency Management

Dependencies are managed via [Poetry](https://python-poetry.org). Run the following [command](https://python-poetry.org/docs/cli/) to export `poetry.lock` file to `requirements.txt` file:
```bash
poetry export -f requirements.txt --output requirements.txt
```
