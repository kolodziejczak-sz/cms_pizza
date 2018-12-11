from .models import Photo
from base.utils import render

def index(request, param = None):
  photos = Photo.objects.all()
  return render(request, 'gallery/index.html', {
    'photos': photos
  })
