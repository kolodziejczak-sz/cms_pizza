from django.db import models
from datetime import date

from tinymce import models as tinymce_models

class Subsite(models.Model):
  title = models.CharField(max_length = 200)
  content = tinymce_models.HTMLField()
  pub_date = models.DateField(default = date.today)
  
  def __str__(self):
    return self.title
