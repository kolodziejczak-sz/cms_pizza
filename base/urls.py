from django.urls import path

from . import views

app_name = 'base'
urlpatterns = [
  path('', views.redirectHome),
  path('<slug:url>', views.index, name='index'),
  path('<slug:url>/<int:param>', views.index, name='index'),
] 