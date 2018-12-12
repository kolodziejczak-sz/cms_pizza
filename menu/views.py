from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import Product, Price, Category
from base.utils import render

def index(request, param = None):
  try:
    categories = Category.objects.all()
    return render(request, 'menu/index.html', {
      'categories': categories
    })
  except:
    return HttpResponseBadRequest()
