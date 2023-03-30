from django.urls import path
from . import views

app_name = 'authe'
urlpatterns = [
    path('join/', views.blank, name='list'),
    path('login/', views.blank, name='list'),
    path('logout', views.blank, name='list'),
    path('', views.blank, name='list'),
]