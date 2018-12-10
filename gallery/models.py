from django.db import models
from datetime import date

class Photo(models.Model):
  image = models.ImageField(upload_to='gallery')
  description = models.TextField(blank = True, max_length=1000)
  pub_date = models.DateField(default = date.today)
  
  def __str__(self):
    if (len(self.description) > 50):
      return self.description[0:47] + '...'
    else:
      return self.description