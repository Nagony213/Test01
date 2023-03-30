from django.urls import path
from . import views

app_name = 'Main'
urlpatterns = [
    path('', views.board_list.as_view(), name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('gethere/', views.gethere, name='gethere'),
    path('schedule/', views.schedule, name='schedule'),
    path('graduate/', views.graduate, name='graduate'),
    path('master/', views.master, name='master'),
    path('lifelong/', views.lifelong, name='lifelong'),
]