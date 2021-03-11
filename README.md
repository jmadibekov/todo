# Todo List Manager

This is a small mini webapp that uses following tools (not an exhaustive list):
- Django & DRF (for the webapp with RESTful API)
- Docker Compose (to isolate multiple stacks)
- Redis (for caching)

The app is (almost) ready for production.

## Getting Started

To build and run the app, clone the repo and use the following command after installing Docker:

```bash
docker-compose up
```

Once it has started, you can open your browser to [http://localhost:8000/api](http://localhost:8000/api).
- You can also head to [http://localhost:8000/admin](http://localhost:8000/admin), but you need to first create superuser for that.

## Testing

The project contains basic tests to check models & API. Run the following command from web container at the Docker to test:
```bash
python manage.py test
```
