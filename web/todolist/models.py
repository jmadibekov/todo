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
    due = models.DateTimeField()

    def clean(self):
        # Due date & time should be no earlier than created_at.
        created_at = self.created_at if self.created_at else timezone.now()
        if self.due < created_at:
            raise exceptions.ValidationError(
                "Due date & time should be no earlier than that the date the todo was created."
            )

    class Type(models.IntegerChoices):
        TODO = 0
        DONE = 1

    type = models.IntegerField(choices=Type.choices, default=Type.TODO)

    def __str__(self):
        return self.title

    # Overriding the save method because clean method needs to be manually called
    def save(self, *args, **kwargs):
        # Validation
        self.clean()
        super().save(*args, **kwargs)  # Call the "real" save() method.

    class Meta:
        ordering = [
            "type",
            "title",
        ]
