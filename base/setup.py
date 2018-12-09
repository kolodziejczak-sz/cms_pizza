from .models import Navigation, Ad, AppConfig

def init_nav():
  if(Navigation.objects.all().count() == 0):
    home = Navigation(
      url = 'home',
      label = 'Home',
      subsite = None,
      sort = 0,
      application = 'contact'
    )
    contact = Navigation(
      url = 'contact',
      label = 'Contact',
      subsite = None,
      sort = 1,
      application = 'contact'
    )
    home.save()
    contact.save()

def init_config():
  if (AppConfig.objects.all().count() == 0):
    cfg = make_default_config()
    cfg.save()

def make_default_config():
  home = Navigation.objects.filter(url = 'home')[:1].get()
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
