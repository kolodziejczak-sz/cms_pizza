from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  def has_add_permission(self, request, obj=None):
    return (Contact.objects.all().count() == 0)

  def has_delete_permission(self, request, obj=None):
    return (Contact.objects.all().count() == 1)

  def changelist_view(self, request, extra_context=None):
    if self.model.objects.all().count() == 1:
      obj = self.model.objects.all()[0]
      return HttpResponseRedirect(reverse("admin:%s_%s_change" %(self.model._meta.app_label, self.model._meta.model_name), args=(obj.id,)))
    return super(ContactAdmin, self).changelist_view(request=request, extra_context=extra_context)

admin.site.register(Contact, ContactAdmin)