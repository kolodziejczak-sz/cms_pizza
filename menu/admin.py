from django.contrib import admin

from .models import MenuConfig, Ingredient, Product, Price, Category, Size

class MenuConfigAdmin(admin.ModelAdmin):

  def has_add_permission(self, request, obj=None):
    return False

  def has_delete_permission(self, request, obj=None):
    return False

  def changelist_view(self, request, extra_context=None):
    if self.model.objects.all().count() == 1:
      obj = self.model.objects.all()[0]
      return HttpResponseRedirect(reverse("admin:%s_%s_change" %(self.model._meta.app_label, self.model._meta.model_name), args=(obj.id,)))
    return super(MenuConfigAdmin, self).changelist_view(request=request, extra_context=extra_context)

class IngredientTabularInline(admin.TabularInline):
  model = Ingredient

class ProductAdmin(admin.ModelAdmin):
  list_display = ('product_label', 'category')
  inlines = [IngredientTabularInline]

class SizeAdmin(admin.ModelAdmin):
  list_display = ('size_label', 'category', 'amount', 'unit_label')

class PriceAdmin(admin.ModelAdmin):
  list_display_links = None
  list_editable = ['amount']
  list_display = ('category', 'product', 'size', 'amount')
  
  def has_add_permission(self, request, obj=None):
    return False

  def has_delete_permission(self, request, obj=None):
    return False

admin.site.register(MenuConfig, MenuConfigAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Category)
