from django.urls import path
from.views import *

urlpatterns = [
    path('create', CreateTodo.as_view()),
    path('',ListToDo.as_view()),
    path('<int:pk>', DetailTodo.as_view()),
    path('delete/<int:pk>', DeleteToDo.as_view())
]