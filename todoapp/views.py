from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from todoapp.models import Todo

def todo_checking(request, id):
    try:
        check = Todo.objects.get(id=id)
        check.done = not check.done  # Flip the value of 'done'
        check.save()
        return HttpResponse("Todo status toggled successfully.")
    except Todo.DoesNotExist:
        return HttpResponse("Todo with the provided ID does not exist.")


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todo_list'
    template_name = 'todoapp/todo_list.html'

