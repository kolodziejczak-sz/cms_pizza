from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import News
from base.utils import render
import math

def index(request, param = None):
  if param:
    return item(request, param)
  else:
    return news_list(request)

def news_list(request):
  page = int(request.GET.get('p', 1))

  items_per_page = 6
  items_count = News.objects.all().count()

  pages_count = math.ceil(items_count / items_per_page)
  idxStart = ((page - 1) * items_per_page)
  idxEnd = (idxStart + (items_per_page - 1))
  print(idxStart,idxEnd)

  news_list = News.objects.all().order_by('pub_date')[idxStart:idxEnd]
  return render(request, 'news/list.html', {
    'news_list': news_list,
    'current_page': page,
    'pages_count': pages_count,
    'pages_range': range(1,pages_count + 1)
  })

def item(request, news_id):
  news = get_object_or_404(News, pk=news_id)
  return render(request, 'news/item.html', {
    'news': news
  })
  