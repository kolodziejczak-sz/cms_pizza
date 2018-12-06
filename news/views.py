from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import News

def list(request):
  news_list = News.objects.all()
  return render(request, 'news/list.html', {
    'news_list': news_list
  })

def item(request, news_id):
  news = get_object_or_404(News, pk=question_id)
  return render(request, 'news/item.html', {
    'news': news
  })
  