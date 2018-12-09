from django.shortcuts import render as django_render
from django.http import HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist

from .models import Navigation, AppConfig, Ad

def get_navigation():
  return Navigation.objects.order_by('sort')

def get_config():
  return AppConfig.objects.all()[:1].get()

def get_ad():
  try:
    return Ad.objects.all()[:1].get()
  except ObjectDoesNotExist:
    return None

def render(request, templateUrl, viewbag = {}):
  #try:
    ad = get_ad()
    cfg = get_config()
    nav = get_navigation()
    return django_render(request, templateUrl, {
      'ad': ad,
      'cfg': cfg,
      'nav': nav,
      'viewbag': viewbag,
    })
  #except Exception:
    #return HttpResponseServerError()



