from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from tinymce import models as tinymce_models

class MenuConfig(models.Model):
  currency_label = models.CharField(default = '$', max_length = 10)
  menu_header = tinymce_models.HTMLField()
  menu_footer = tinymce_models.HTMLField()

  def __str__(self):
    return 'Menu config'

class Category(models.Model):
  category_label = models.CharField(max_length = 100)
  photo = models.ImageField(blank = True, upload_to = 'menu')
  sort = models.PositiveIntegerField(default = 0)
  
  class Meta(object):
    ordering = ['sort']
    
  def __str__(self):
    return self.category_label

class Size(models.Model):
  category = models.ForeignKey(Category, on_delete = models.CASCADE)
  amount = models.IntegerField(blank = True)
  unit_label = models.CharField(max_length = 100, blank = True)
  size_label = models.CharField(max_length = 100)
  sort = models.PositiveIntegerField(default = 0)
  
  class Meta(object):
    ordering = ['sort']

  def __str__(self):
    return self.size_label

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete = models.CASCADE)
  product_label = models.CharField(max_length = 100)
  extra_info = models.TextField(max_length = 400, blank = True)
  sort = models.PositiveIntegerField(default = 0)
  
  class Meta(object):
    ordering = ['sort']

  def __str__(self):
    return self.product_label

class Ingredient(models.Model):
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  ingredient_label = models.CharField(max_length = 100)

  def __str__(self):
    return self.ingredient_label

class Price(models.Model):
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  size = models.ForeignKey(Size, on_delete = models.CASCADE)
  amount = models.DecimalField(max_digits = 6, decimal_places = 2)

  def category(self):
    return self.product.category

  def __str__(self):
    return str(self.amount)


@receiver(post_save, sender=Size)
def afterNewSize(sender, instance, **kwargs):
  if kwargs['created']:
    category = instance.category
    products = Product.objects.filter(category__id = category.id)
    for p in products:
      price = Price(product = p, size = sender, amount = 0)
      price.save()

@receiver(post_save, sender=Product)
def afterNewProduct(sender, instance, **kwargs):
  if kwargs['created']:
    category = instance.category
    sizes = Size.objects.filter(category__id = category.id)
    for s in sizes:
      price = Price(product = instance, size = s, amount = 0)
      price.save()








