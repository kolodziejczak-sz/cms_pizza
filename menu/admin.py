from django.contrib import admin

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MenuConfig, Ingredient, Product, Price, Category, Size
from adminsortable2.admin import SortableAdminMixin

class ProductCategoryListFilter(admin.SimpleListFilter):
  title = 'Category'
  parameter_name = 'category'

  def lookups(self, request, model_admin):
    categories = Category.objects.all()
    categories_fields = []

    for c in categories:
      categories_fields.append([c.category_label.lower(), c.category_label])
    return categories_fields

  def queryset(self, request, queryset):
    if self.value():
      selected_category = Category.objects.filter(category_label__iexact = self.value())[0]
      return queryset.filter(category = selected_category)
    return queryset

class PriceCategoryListFilter(admin.SimpleListFilter):
  title = 'Category'
  parameter_name = 'category'

  def lookups(self, request, model_admin):
    categories = Category.objects.all()
    categories_fields = []

    for c in categories:
      categories_fields.append([c.category_label.lower(), c.category_label])
    return categories_fields

  def queryset(self, request, queryset):
    if self.value():
      selected_category = Category.objects.filter(category_label__iexact = self.value())[0]
      return queryset.filter(product__category = selected_category)
    return queryset

class SizeCategoryListFilter(admin.SimpleListFilter):
  title = 'Category'
  parameter_name = 'category'

  def lookups(self, request, model_admin):
    categories = Category.objects.all()
    categories_fields = []

    for c in categories:
      categories_fields.append([c.category_label.lower(), c.category_label])
    return categories_fields

  def queryset(self, request, queryset):
    if self.value():
      selected_category = Category.objects.filter(category_label__iexact = self.value())[0]
      return queryset.filter(category = selected_category)
    return queryset


@admin.register(MenuConfig)
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

@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
  list_display = ('sort', 'product_label', 'category')
  list_filter = (ProductCategoryListFilter,)
  inlines = [IngredientTabularInline]

@admin.register(Size)
class SizeAdmin(SortableAdminMixin, admin.ModelAdmin):
  list_display = ('sort', 'size_label', 'category', 'amount', 'unit_label')
  list_filter = (SizeCategoryListFilter,)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
  list_display_links = None
  list_editable = ['amount']
  list_display = ('category', 'product', 'size', 'amount')
  list_filter = (PriceCategoryListFilter,)
  
  def has_add_permission(self, request, obj=None):
    return False

  def has_delete_permission(self, request, obj=None):
    if "category" in request.__str__():
      return True
    return False


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
  list_display = ('sort', 'category_label')
