from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class board_data(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  assign = models.CharField(max_length=20)
  cat = models.CharField(max_length=20, null=True)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
  def __str__(self):
    return 'BID:{0}, Board:{1} / [{2} - {3}]'.format(self.id, self.assign, self.title, self.author)

  def get_absolute_url(self):
    return '/board/{0}/{1}'.format(self.assign, self.pk)
