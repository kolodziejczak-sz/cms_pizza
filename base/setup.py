from .models import Navigation, Ad, AppConfig

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
  menu = Navigation.objects.filter(url = 'menu')[:1].get()
  cfg = AppConfig(
    title = 'Unititled CMS Pizzeria',
    logo_text =  'LOGO TEXT',
    homepage = menu,
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

def clear_nav():
  Navigation.objects.all().delete()

def clear_config():
  AppConfig.objects.all().delete()

def init(clear = False):
  if clear:
    clear_config()
    clear_nav()
  init_nav()
  init_config()
