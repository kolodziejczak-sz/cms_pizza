from datetime import datetime
from django.http import Http404, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from base.utils import render
from base.models import Navigation

def index(request, url):
  try:
    print(url)
    navItem = Navigation.objects.filter(url = url)[:1].get()
    return render(request, 'subsite/index.html', {
      'item': navItem.subsite
    })
  except ObjectDoesNotExist:
    raise Http404  
