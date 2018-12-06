from django.db import models
from datetime import date
from tinymce import models as tinymce_models

class News(models.Model):
  headline = models.CharField(max_length = 200)
  image = models.ImageField(blank = True)
  lead_sentence = models.CharField(max_length = 600, blank = True)
  content = tinymce_models.HTMLField()
  pub_date = models.DateField(default = date.today)
  
  def __str__(self):
    return self.headline