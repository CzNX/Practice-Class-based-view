from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  
  def __str__(self):
    return self.title


  # def get_absolute_url(self):
  #   return reverse('detail',kwargs={'pk':self.pk})  