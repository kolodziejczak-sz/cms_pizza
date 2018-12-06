from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('news', include('news.urls')),
    path('contact', include('contact.urls')),
    path(r'^tinymce/', include('tinymce.urls')),

]
