from pyexpat import model
from rest_framework import serializers
from .models import Todo, TodoItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'user']
        extra_kwargs = {
            'user': {'read_only': True},
            'description': {'required': False, 'allow_blank': True}
        }


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'