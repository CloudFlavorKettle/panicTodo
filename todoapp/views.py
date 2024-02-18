from celery import shared_task
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from todoapp.models import Todo


def todo_checking(request):
    try:
        check = Todo.objects.get(id=id)
        check.done = not check.done
        check.save()
        return HttpResponse("Todo status toggled successfully.")
    except Todo.DoesNotExist:
        return HttpResponse("Todo with the provided ID does not exist.")


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todo_list'
    template_name = 'todoapp/todo_list.html'


@shared_task
def check_panic_time_and_send_notification():
    todos = Todo.objects.all()
    for todo in todos:
        if todo.panic_time <= timezone.now():
            send_panic_notification(todo)


def send_panic_notification(todo):
    # 이메일이나 다른 방법으로 알림을 보냅니다.
    pass
