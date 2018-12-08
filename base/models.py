from django.db import models
from datetime import date

from tinymce import models as tinymce_models
from colorful.fields import RGBColorField
from django.core.validators import MinValueValidator, MaxValueValidator

from subsite.models import Subsite

class Navigation(models.Model):
  url = models.SlugField(max_length = 40, unique = True)
  label = models.CharField(max_length = 50)
  subsite = models.ForeignKey(Subsite, on_delete = models.DO_NOTHING)
  sort = models.PositiveIntegerField(default = 0, blank = False, null = False)

  class Meta(object):
    ordering = ['sort']

  def __str__(self):
    return self.label


class Ad(models.Model):
  content = tinymce_models.HTMLField()

  def __str__(self):
    return 'Ad'

class AppConfig(models.Model):
  title = models.CharField(max_length = 120)
  logo_image = models.ImageField(blank = True, upload_to='media/config')
  logo_text =  models.CharField(max_length = 40)
  baner_image = models.ImageField(blank = True, upload_to='media/config')
  baner_text = tinymce_models.HTMLField(blank = True)

  background_color = RGBColorField()
  accent_color_1 = RGBColorField()
  accent_color_2 = RGBColorField()
  text_color_1 = RGBColorField()
  text_color_2 = RGBColorField()

  small_font_size = models.IntegerField(default=11,validators=[
    MinValueValidator(6),
    MaxValueValidator(12)
  ])
  normal_font_size = models.IntegerField(default=14,validators=[
    MinValueValidator(12),
    MaxValueValidator(18)
  ])
  big_font_size = models.IntegerField(default=22,validators=[
    MinValueValidator(18),
    MaxValueValidator(36)
  ])

  def __str__(self):
    return 'App config'