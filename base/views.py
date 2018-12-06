from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import Navigation, Ad, AppConfig

def index(request):
  try:
    cfg = get_config()
    return render(request, 'base/index.html', {
      'nav': get_navigation(),
      'cfg': cfg
    })
  except ObjectDoesNotExist:
    return HttpResponseBadRequest


def ad(request):
  try:
    ad = Ad.objects.all()[:1].get()
    return render(request, 'base/ad.html', {
      'ad': ad
    })
  except ObjectDoesNotExist:
    return render(request, 'base/ad.html')

def get_navigation():
  return Navigation.objects.order_by('sort')

def get_config():
  return AppConfig.objects.all()[:1].get()