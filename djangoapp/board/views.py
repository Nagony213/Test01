from django.shortcuts import render
from board.models import board_data
from django.views.generic import DetailView, ListView

class board_list(ListView):
  template_name = 'board/list.html'
  context_object_name = 'object_list'
  paginate_by = 10

  def get_queryset(self):
    return board_data.objects.filter(assign=self.kwargs['bd']).order_by('-pk')
  
class board_detail(DetailView):
  model = board_data
  template_name = 'board/detail.html'