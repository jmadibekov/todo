from django.db import models


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
