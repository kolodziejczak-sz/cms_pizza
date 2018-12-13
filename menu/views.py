from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import Product, Price, Category, Size, Ingredient
from base.utils import render, AttrDict

def get_products_by_category(category):
  bag = []
  products = Product.objects.filter(category = category)
  sizes = Size.objects.filter(category = category)
  for p in products:
    product = AttrDict({
      'product_label': p.product_label,
      'ingredients': Ingredient.objects.filter(product = p),
      'sizes': sizes,
      'prices': Price.objects.filter(product = p).order_by('size')
    })
    bag.append(product)
  return bag

def render_by_category(request, category):
  return render(
    request,
    'menu/table.html',
    get_products_by_category(category)
  )

def render_categories(request):
  return render(request, 'menu/categories.html', {
    'categories': Category.objects.all() 
  })

def index(request, param = None):
  category_str = request.GET.get('category', None)
  if category_str is None:
    return render_categories(request)

  category = Category.objects.filter(category_label__iexact = category_str)[0]
  return render_by_category(request, category)
