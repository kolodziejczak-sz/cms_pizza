from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
  name = models.CharField(max_length = 200)
  telephone = PhoneNumberField(blank = True)
  email = models.EmailField(max_length = 254)
  city = models.CharField(max_length = 200)
  address = models.CharField(max_length = 200)
  latitude = models.DecimalField(blank = True, max_digits=9, decimal_places=6, null = True)
  longitude = models.DecimalField(blank = True, max_digits=9, decimal_places=6, null = True)

  def __str__(self):
    return self.city + ' ' + self.address

class Message(models.Model):
  email = models.EmailField(max_length = 254, blank = True)
  subject = models.CharField(max_length = 200)
  message = models.TextField(max_length = 1000)
  date = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
    return self.subject