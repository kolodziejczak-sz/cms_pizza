from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Contact(models.Model):
  telephone = PhoneNumberField(blank = True)
  email = models.EmailField(max_length = 254, blank = True)
  city = models.CharField(max_length = 200)
  address = models.CharField(max_length = 200)

  def __str__(self):
    return self.city + ' ' + self.address