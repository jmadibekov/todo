from rest_framework import viewsets

from .models import Category, Todo
from .serializers import CategorySerializer, TodoSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be CRUD.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be CRUD.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
