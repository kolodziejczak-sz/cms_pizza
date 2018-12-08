from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseBadRequest, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist

from .models import Navigation, Ad, AppConfig
from .utils import render

def index(request):
  try:
    return render(request, 'base/base.html')
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