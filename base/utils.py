from django.shortcuts import render as django_render
from django.http import HttpResponseServerError

from .models import Navigation, AppConfig

def get_navigation():
  return Navigation.objects.order_by('sort')

def get_config():
  return AppConfig.objects.all()[:1].get()

def render(request, templateUrl, viewbag = {}):
  #try:
    cfg = get_config()
    nav = get_navigation()
    return django_render(request, templateUrl, {
      'cfg': cfg,
      'nav': nav,
      'viewbag': viewbag,
    })
  #except Exception:
    #return HttpResponseServerError()



