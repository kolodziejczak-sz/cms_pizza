from django.contrib import admin

from .models import Ingredient, Product, Price, Category, Size

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

admin.site.register(Price, PriceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Category)
