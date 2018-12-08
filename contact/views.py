from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from base.utils import render
from .models import Contact

def index(request):
  try:
    contact = Contact.objects.all()[:1].get()
    return render(request, 'contact/index.html', {
      'contact': contact
    })
  except ObjectDoesNotExist:
    return render(request, 'contact/index.html')