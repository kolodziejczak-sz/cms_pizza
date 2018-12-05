from django.urls import path

from . import views

app_name = 'base'
urlpatterns = [
  path('', views.index, name='index'),
  path('contact', views.contact, name='contact'),
  path('news', views.news_list, name='news_list'),
  path('news/<int:id>', views.news, name='news'),
  path('page/<slug:url>', views.subsite, name='subsite'),
]