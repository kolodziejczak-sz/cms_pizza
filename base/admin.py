from django.contrib import admin

# Register your models here.
from .models import Navigation, Subsite

class NavigationAdmin(admin.ModelAdmin):
  list_display = ('label', 'subsite', 'url', 'sort')

admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Subsite)
