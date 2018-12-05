from django.shortcuts import render
from datetime import datetime
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Navigation, Subsite, Contact

def index(request):
  return render(request, 'base/index.html', {
    'nav': get_navigation()
  })

def contact(request):
  try:
    contact = Contact.objects.all()[:1].get()
    return render(request, 'base/contact.html', {
      'contact': contact
    })
  except ObjectDoesNotExist:
    return render(request, 'base/contact.html')
  

def subsite(request, url):
  try:
    navItem = Navigation.objects.filter(url = url)[:1].get()
    return render(request, 'base/subsite.html', {
      'item': navItem.subsite
    })
  except ObjectDoesNotExist:
    raise Http404  

def get_navigation():
  return Navigation.objects.order_by('sort')