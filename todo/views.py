from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Todo, TodoItem
from .serializers import TodoSerializer, TodoItemSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated




def todo_page(request):
    return render(request, 'index.html')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("🔥 Serializer Errors:", serializer.errors)  # این لاگ رو نگاه کن بعد از POST
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer

    def get_queryset(self):
        todo_id = self.kwargs["todo_pk"]
        return TodoItem.objects.filter(todo_id=todo_id)

    def perform_create(self, serializer):
        todo_id = self.kwargs["todo_pk"]
        serializer.save(todo_id=todo_id)


