from django.shortcuts import render
from rest_framework import generics
from .serializers import * 
from .models import *
# Create your views here.
class CreateTodo(generics.CreateAPIView): #create
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ListToDo(generics.ListAPIView): #read
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView): #update
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteToDo(generics.DestroyAPIView): #delete
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
