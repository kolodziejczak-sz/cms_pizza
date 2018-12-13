from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from cms_pizza.setup import init

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from adminsortable2.admin import SortableAdminMixin

from .models import Navigation, Ad, AppConfig

@admin.register(Navigation)
class NavigationAdmin(SortableAdminMixin,admin.ModelAdmin):
  list_display = ('sort', 'label', 'subsite', 'application', 'url', 'visible')
  list_editable = ['visible']
  
  def has_delete_permission(self, request, obj=None):
    if(obj and obj.subsite is None):
      return False
    else:
      return True

  def get_fieldsets(self, request, obj=None):
    if(obj and obj.subsite is None):
      return [(obj.application.capitalize() + ' Application', {'fields': [ 'label', 'url', 'visible' ]})]
    else:
      return [(None, {'fields': [ 'label', 'url', 'subsite', 'visible' ]})]

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
  def has_add_permission(self, request, obj=None):
    return (Ad.objects.all().count() == 0)
  def has_delete_permission(self, request, obj=None):
    return (Ad.objects.all().count() == 1)
  def changelist_view(self, request, extra_context=None):
    if self.model.objects.all().count() == 1:
      obj = self.model.objects.all()[0]
      return HttpResponseRedirect(reverse("admin:%s_%s_change" %(self.model._meta.app_label, self.model._meta.model_name), args=(obj.id,)))
    return super(AdAdmin, self).changelist_view(request=request, extra_context=extra_context)
  
@admin.register(AppConfig)
class AppConfigAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Basic config data', {'fields': [
      'title', 'logo_image', 'logo_text', 'favicon', 'homepage', 'currency_label'
    ]}),
    ('Design', {'fields': [
      'background_image','background_color', 'accent_color_1', 'accent_color_2', 'accent_color_3', 'text_color_1', 'text_color_2'
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

init()

admin.site.unregister(User)
admin.site.unregister(Group)
