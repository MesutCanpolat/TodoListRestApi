from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from todos.models import Todo
from todos.pagenations import StandardResultsSetPagination
from todos.serializer import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination