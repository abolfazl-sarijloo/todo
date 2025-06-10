from pyexpat import model
from rest_framework import serializers
from .models import Todo, TodoItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description','completed', 'user']
        extra_kwargs = {
            'user': {'read_only': True},
            'description': {'required': False, 'allow_blank': True}
        }


# serializers.py
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        extra_kwargs = {
            'todo': {'read_only': True}, 
            'description': {'required': False, 'allow_blank': True}
        }
