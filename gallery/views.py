from .models import Photo
from base.utils import render

def index(request):
  photos = Photo.objects.all()
  return render(request, 'gallery/index.html', {
    'photos': photos
  })
