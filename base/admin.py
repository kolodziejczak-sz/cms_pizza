from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Navigation, Ad, AppConfig

class NavigationAdmin(admin.ModelAdmin):
  list_display = ('label', 'subsite', 'url', 'sort')

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

  def changelist_view(self, request, extra_context=None):
    if self.model.objects.all().count() == 1:
      obj = self.model.objects.all()[0]
      return HttpResponseRedirect(reverse("admin:%s_%s_change" %(self.model._meta.app_label, self.model._meta.model_name), args=(obj.id,)))
    return super(AppConfigAdmin, self).changelist_view(request=request, extra_context=extra_context)


admin.site.register(AppConfig, AppConfigAdmin)
admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Ad, AdAdmin)

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