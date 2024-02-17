from django.urls import path
from django.contrib.auth import views as auth_views

from accountapp import views

app_name = 'accountapp'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]
