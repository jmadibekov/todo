from django.core import exceptions
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = [
            "name",
        ]


class Todo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(default=timezone.now)

    def clean(self):
        # Due date & time should be no earlier than created_at.
        if self.due < self.created_at:
            raise exceptions.ValidationError(
                "Due date & time should be no earlier than that the date the todo was created."
            )

    class Type(models.IntegerChoices):
        TODO = 0
        DONE = 1

    type = models.IntegerField(choices=Type.choices, default=Type.TODO)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "type",
            "title",
        ]
