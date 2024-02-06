from django.shortcuts import render
from django.views.generic import ListView

from todoapp.models import Todo


# Create your views here.
class TodoListView(ListView):
    model = Todo
    context_object_name = 'todoapp/todo_list.html'
