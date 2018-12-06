from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
  path('', views.list, name='list'),
  path('<int:id>', views.item, name='item'),
]