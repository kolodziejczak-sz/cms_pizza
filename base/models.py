from django.db import models
from tinymce import models as tinymce_models
from positions.fields import PositionField

class Subsite(models.Model):
  title = models.CharField(max_length=200)
  content = tinymce_models.HTMLField()
  pub_date = models.DateTimeField('date published')

class NavigationItem(models.Model):
  label = models.CharField(max_length=50)
  subsite = models.ForeignKey(Subsite, unique=True, on_delete=models.DO_NOTHING)
  sort = PositionField(collection='subsite')
  


