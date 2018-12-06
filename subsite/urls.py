from django.urls import path

from . import views

app_name = 'subsite'
urlpatterns = [
  path('<slug:url>', views.index, name='index')
]