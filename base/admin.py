from django.contrib import admin

# Register your models here.
from .models import Navigation, Subsite, Contact, News, Ad, AppConfig

class NavigationAdmin(admin.ModelAdmin):
  list_display = ('label', 'subsite', 'url', 'sort')

class ContactAdmin(admin.ModelAdmin):
  def has_add_permission(self, request, obj=None):
    return (Contact.objects.all().count() == 0)
  def has_delete_permission(self, request, obj=None):
    return (Contact.objects.all().count() == 1)

class AdAdmin(admin.ModelAdmin):
  def has_add_permission(self, request, obj=None):
    return (Ad.objects.all().count() == 0)
  def has_delete_permission(self, request, obj=None):
    return (Ad.objects.all().count() == 1)

class AppConfigAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Basic config data', {'fields': [
      'title', 'logo_image', 'logo_text', 'baner_image', 'baner_text'
    ]}),
    ('Colors', {'fields': [
      'background_color', 'accent_color_1', 'accent_color_2', 'text_color_1', 'text_color_2'
    ]}),
    ('Font sizes [px]', {'fields': [
      'big_font_size', 'normal_font_size', 'small_font_size'
    ]}),
  ]
  def has_add_permission(self, request, obj=None):
    return False
  def has_delete_permission(self, request, obj=None):
    return False


admin.site.register(AppConfig, AppConfigAdmin)
admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(News)
admin.site.register(Subsite)

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