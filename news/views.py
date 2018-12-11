from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import News
from base.utils import render

def index(request, param = None):
  if param:
    return item(request, param)
  else:
    return news_list(request)

def news_list(request):
  news_list = News.objects.all()
  return render(request, 'news/list.html', {
    'news_list': news_list
  })

def item(request, news_id):
  news = get_object_or_404(News, pk=news_id)
  return render(request, 'news/item.html', {
    'news': news
  })
  