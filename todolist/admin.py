from django.contrib import admin

from .models import Category, Todo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "parent",
    )


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "notes",
        "category",
    )
