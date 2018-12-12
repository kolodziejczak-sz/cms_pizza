from .models import Photo

desc = [
  "Sed ut perspiciatis unde omnis iste natus error",
  "quae ab illo inventore veritatis et quasi architecto",
  "aspernatur aut odit aut fugit",
  "est, qui dolorem ipsum quia dolor sit amet",
  "et dolore magnam aliquam quaerat voluptatem",
  "nisi ut aliquid ex ea commodi consequatur",
  "aspernatur aut odit aut fugit",
  "est, qui dolorem ipsum quia dolor sit amet"
]

def make_photo(url, desc):
  photo = Photo(image = url, description = desc)
  photo.save()

def init_photo():
  if (Photo.objects.all().count() == 0):
    for i in range(0, 8):
      make_photo('gallery/pizza'+str(i+1)+'.jpg', desc[i])

def clear_photo():
  Photo.objects.all().delete()

def init(clear = False):
  if clear:
    clear_photo()
  init_photo()