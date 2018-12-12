from .models import Contact

def init_contact():
  if(Contact.objects.all().count() == 0):
    item = Contact(
      name = 'Pizzeria Limited Company',
      email = 'your_email@sample.uk',
      city = 'Poznan',
      address = 'Mostowa 1111',
      latitude = -25.363,
      longitude = 131.044
    )
    item.save()

def clear_contact():
  Contact.objects.all().delete()

def init(clear = False):
  if clear:
    clear_contact()
  init_contact()