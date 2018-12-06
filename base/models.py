from django.db import models
from datetime import date

from tinymce import models as tinymce_models
from phonenumber_field.modelfields import PhoneNumberField
from colorful.fields import RGBColorField
from django.core.validators import MinValueValidator, MaxValueValidator

class Contact(models.Model):
  telephone = PhoneNumberField(blank = True)
  email = models.EmailField(max_length = 254, blank = True)
  city = models.CharField(max_length = 200)
  address = models.CharField(max_length = 200)

  def __str__(self):
    return self.city + ' ' + self.address


class News(models.Model):
  headline = models.CharField(max_length = 200)
  image = models.ImageField(blank = True)
  lead_sentence = models.CharField(max_length = 600, blank = True)
  content = tinymce_models.HTMLField()
  pub_date = models.DateField(default = date.today)
  
  def __str__(self):
    return self.headline


class Subsite(models.Model):
  title = models.CharField(max_length = 200)
  content = tinymce_models.HTMLField()
  pub_date = models.DateField(default = date.today)
  
  def __str__(self):
    return self.title

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
  logo_image = models.ImageField(blank = True)
  logo_text =  models.CharField(max_length = 40)
  baner_image = models.ImageField(blank = True)
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