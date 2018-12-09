from django.shortcuts import get_object_or_404, redirect
from datetime import datetime
from django.http import Http404, HttpResponseBadRequest, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist

from .models import Navigation, Ad, AppConfig
from .utils import render

from contact import views as contact
from news import views as news
from subsite import views as subsite 

views = {
  'contact': contact,
  'news': news,
  'subsite': subsite,
}

def redirectHome(request):
  config = AppConfig.objects.all()[:1].get()
  return redirect('/page/' + config.homepage.url)

def index(request, url):
  try:
    link = Navigation.objects.filter(visible = True, url = url)[:1].get()
    if(link.subsite is None):
      return views[link.application].index(request)
    else:
      return render(request, 'subsite/index.html', {
        'item': link.subsite
      })
  except ObjectDoesNotExist:
    raise Http404

def ad(request):
  try:
    ad = Ad.objects.all()[:1].get()
    return render(request, 'base/ad.html', {
      'ad': ad
    })
  except ObjectDoesNotExist:
    return render(request, 'base/ad.html')