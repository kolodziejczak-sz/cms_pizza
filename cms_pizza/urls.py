from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', include('base.urls')),
    path('api/', include('contact.urls')),
    path(r'tinymce/', include('tinymce.urls')),
    path('', include('base.urls')),
] + static('/media/', document_root=BASE_DIR+'/media')