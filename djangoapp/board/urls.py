from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('<str:bd>', views.board_list.as_view(), name='list'),
    path('<str:bd>/<int:pk>', views.board_detail.as_view(), name='detail'),
]