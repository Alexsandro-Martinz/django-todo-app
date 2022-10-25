from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TodoSerialiazer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerialiazer
    queryset = Todo.objects.all()
    
