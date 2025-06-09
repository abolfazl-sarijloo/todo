# todo/urls.py
from django.urls import path, include
from .views import todo_page, TodoViewSet, TodoItemViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'todos', TodoViewSet, basename='todo')

nested_router = routers.NestedSimpleRouter(router, r'todos', lookup='todo')
nested_router.register(r'items', TodoItemViewSet, basename='todo-items')

urlpatterns = [
    path('', todo_page, name='todo-page'),
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]

urlpatterns += router.urls + nested_router.urls
