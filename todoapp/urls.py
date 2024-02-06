from django.urls import path

from todoapp import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo'),
    path('todo-checking/<int:id>/', views.todo_checking, name='todo_checking'),
]
