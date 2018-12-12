from django.db import models

class Category(models.Model):
  category_label = models.CharField(max_length = 100)

  def __str__(self):
    return self.category_label

class Size(models.Model):
  category = models.ForeignKey(Category, on_delete = models.CASCADE)
  size_label = models.CharField(max_length = 100)

  def __str__(self):
    return self.size_label

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete = models.CASCADE)
  product_label = models.CharField(max_length = 100)

  def __str__(self):
    return self.product_label

class Ingredient(models.Model):
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  ingredient_label = models.CharField(max_length = 100)

  def __str__(self):
    return self.ingredient_label

class Price(models.Model):
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  category = models.ForeignKey(Category, on_delete = models.CASCADE)
  amount = models.DecimalField(max_digits = 6, decimal_places = 2)
  currency = models.CharField(max_length = 100)