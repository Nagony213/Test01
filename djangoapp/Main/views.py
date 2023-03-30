from django.shortcuts import render
from board.models import board_data
from django.views.generic import DetailView, ListView

class board_list(ListView):
  template_name = 'Main/index.html'
  context_object_name = 'object_list'

  def get_queryset(self):
    queryset = {'notice': board_data.objects.filter(assign='notice').order_by('-pk')[:4],
                'news': board_data.objects.filter(assign='news').order_by('-pk')[:4],
                'free': board_data.objects.filter(assign='free').order_by('-pk')[:4],
                }
    return queryset

def greeting(request):
  return render(request, 'Main/common/1greeting.html')

def gethere(request):
  return render(request, 'Main/common/2gethere.html')

def schedule(request):
  return render(request, 'Main/common/3schedule.html')

def graduate(request):
  return render(request, 'Main/common/4graduate.html')

def master(request):
  return render(request, 'Main/common/5master.html')

def lifelong(request):
  return render(request, 'Main/common/6lifelong.html')

def notice(request):
  return render(request, 'Main/common/notice.html')

def free(request):
  return render(request, 'Main/common/free.html')