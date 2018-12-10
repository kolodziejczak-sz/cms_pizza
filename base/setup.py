from .models import Navigation, Ad, AppConfig
i = 0

def init_nav():
  if(Navigation.objects.all().count() == 0):
    make_nav('contact')
    make_nav('gallery')

def make_nav(application):
  item = Navigation(
    url = application, 
    label = application.capitalize(),
    subsite = None,
    sort = i,
    application = application
  )
  item.save()
  i = i + 1

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
    accent_color_2 = '#006600',
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
  init_nav()
  init_config()
