from django.contrib import admin

# Register your models here.
from .models import Navigation, Subsite, Contact

class NavigationAdmin(admin.ModelAdmin):
  list_display = ('label', 'subsite', 'url', 'sort')

class ContactAdmin(admin.ModelAdmin):
  def has_add_permission(self, request, obj=None):
        return (Contact.objects.all().count() == 0)
  def has_delete_permission(self, request, obj=None):
        return (Contact.objects.all().count() == 1)

admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Subsite)
admin.site.register(Contact)
