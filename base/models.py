from django.db import models
from datetime import date
from tinymce import models as tinymce_models

class Subsite(models.Model):
  title = models.CharField(max_length=200)
  content = tinymce_models.HTMLField()
  pub_date = models.DateField(default=date.today)
  
  def __str__(self):
    return self.title

class Navigation(models.Model):
  url = models.SlugField(max_length=40, unique=True)
  label = models.CharField(max_length=50)
  subsite = models.ForeignKey(Subsite, on_delete=models.DO_NOTHING)
  sort = models.PositiveIntegerField(default=0, blank=False, null=False)

  class Meta(object):
    ordering = ['sort']

  def __str__(self):
    return self.label
