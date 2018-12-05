from django.contrib import admin

# Register your models here.
from .models import Navigation, Subsite, Contact, News, Ad

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

admin.site.register(Ad, AdAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Navigation, NavigationAdmin)
admin.site.register(News)
admin.site.register(Subsite)
