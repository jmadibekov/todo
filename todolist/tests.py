from datetime import datetime

from django.core import exceptions
from django.test import TestCase
from django.utils import timezone

from .models import Category, Todo


class TodoTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Test")

    def test_due_date_later_than_created(self):
        category = Category.objects.get(name="Test")
        todo = Todo.objects.create(
            title="To do test",
            category=category,
            due=datetime(year=2030, month=1, day=1, tzinfo=timezone.utc),
        )

        print(f"{todo.created_at=}, {todo.due=}")

        with self.assertRaises(exceptions.ValidationError):
            Todo.objects.create(
                title="A",
                category=category,
                due=datetime(year=2010, month=1, day=1, tzinfo=timezone.utc),
            )
