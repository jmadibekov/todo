import json
from datetime import datetime

from django.core import exceptions
from django.test import Client, TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse

from .models import Category, Todo
from .serializers import TodoSerializer

client = Client()


class TodoTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Test")
        due = datetime(year=2030, month=1, day=1, tzinfo=timezone.utc)
        Todo.objects.create(
            title="A",
            category=category,
            due=due,
        )
        Todo.objects.create(
            title="B",
            category=category,
            due=due,
        )
        Todo.objects.create(
            title="C",
            category=category,
            due=due,
        )

        self.valid_payload = {
            "title": "A",
            "category": 1,
            "due": "2030-03-11T19:00:00+06:00",
        }
        self.invalid_payload = {
            "title": "A",
            "category": 1,
            "due": "2010-03-11T19:00:00+06:00",
        }

    def test_due_date_later_than_created(self):
        category = Category.objects.get(name="Test")
        with self.assertRaises(exceptions.ValidationError):
            Todo.objects.create(
                title="A",
                category=category,
                due=datetime(year=2010, month=1, day=1, tzinfo=timezone.utc),
            )

    def test_api_get_todo_list(self):
        # get API response
        response = client.get(reverse("todo-list"))
        # get data from db
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_get_todo_detail(self):
        todo = Todo.objects.get(title="A")
        response = client.get(reverse("todo-detail", kwargs={"pk": todo.pk}))
        serializer = TodoSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Invalid pk
        response = client.get(reverse("todo-detail", kwargs={"pk": -1}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_create_todo(self):
        response = client.post(
            reverse("todo-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = client.post(
            reverse("todo-list"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
