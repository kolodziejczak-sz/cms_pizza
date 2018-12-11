from .models import Navigation, Ad, AppConfig
from gallery.models import Photo


def init_nav():
  if(Navigation.objects.all().count() == 0):
    make_nav('menu',1)
    make_nav('news',2)
    make_nav('gallery',3)
    make_nav('contact',4)

def make_nav(application, sort):
  item = Navigation(
    url = application, 
    label = application.capitalize(),
    subsite = None,
    sort = sort,
    application = application
  )
  item.save()


def init_config():
  if (AppConfig.objects.all().count() == 0):
    cfg = make_default_config()
    cfg.save()

def make_default_config():
  home = Navigation.objects.filter(url = 'contact')[:1].get()
  cfg = AppConfig(
    title = 'Unititled CMS Pizzeria',
    logo_text =  'LOGO TEXT',
    homepage = home,
    background_color = '#FFFFEC',
    accent_color_1 = '#CC0000',
    accent_color_2 = '#51AA51',
    accent_color_3 = '#FFFFFF',
    text_color_1 = '#6C644F',
    text_color_2 = '#9C9178'
  )
  cfg.logo_image = 'config/logo.png'
  cfg.background_image = 'config/background.jpg'
  return cfg

def init():
  #AppConfig.objects.all().delete()
  #Navigation.objects.all().delete()
  #Photo.objects.all().delete()
  init_photo()
  init_nav()
  init_config()


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

def init_photo():
  if (Photo.objects.all().count() == 0):
    for i in range(0, 8):
      make_photo('gallery/pizza'+str(i+1)+'.jpg', desc[i])


def make_photo(url, desc):
  photo = Photo(image = url, description = desc)
  photo.save()

