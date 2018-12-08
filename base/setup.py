from .models import Navigation, Ad, AppConfig

def init_config():
  if (AppConfig.objects.all().count() == 0):
    cfg = make_default_config()
    cfg.save()

def make_default_config():
  return AppConfig(
    title = 'Unititled CMS Pizzeria',
    logo_text =  'LOGO TEXT',
    baner_text = 'BANER TEXT',
    background_color = '#FFFFEC',
    accent_color_1 = '#CC0000',
    accent_color_2 = '#006600',
    text_color_1 = '#6C644F',
    text_color_2 = '#9C9178'
  )

init_config()