from rest_framework import serializers

from .models import Category, Todo


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
