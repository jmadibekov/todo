from rest_framework import serializers

from .models import Category, Todo


class CategorySerializer(serializers.ModelSerializer):
    chain = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_chain(self, obj):
        chain = []
        while obj:
            chain.append((obj.name, obj.id))
            obj = obj.parent
        return chain


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
