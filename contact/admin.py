from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Contact, Message

class ContactAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Contact', {'fields': [
      'name', 'telephone', 'email', 'city', 'address'
    ]}),
    ('Coordinates (fill if you want Google maps widget)', {'fields': [
      'latitude', 'longitude'
    ]}),
  ]

  def has_add_permission(self, request, obj=None):
    return (Contact.objects.all().count() == 0)

  def has_delete_permission(self, request, obj=None):
    return (Contact.objects.all().count() == 1)

  def changelist_view(self, request, extra_context=None):
    if self.model.objects.all().count() == 1:
      obj = self.model.objects.all()[0]
      return HttpResponseRedirect(reverse("admin:%s_%s_change" %(self.model._meta.app_label, self.model._meta.model_name), args=(obj.id,)))
    return super(ContactAdmin, self).changelist_view(request=request, extra_context=extra_context)

class MessageAdmin(admin.ModelAdmin):
  list_display = ('email', 'subject', 'date')

  def has_add_permission(self, request, obj=None):
    return False

admin.site.register(Contact, ContactAdmin)
admin.site.register(Message, MessageAdmin)