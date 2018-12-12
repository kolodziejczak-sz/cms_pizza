from .models import Product, Ingredient, Price, Category, Size

class AttrDict(dict):
  def __init__(self, *args, **kwargs):
      super(AttrDict, self).__init__(*args, **kwargs)
      self.__dict__ = self

def make_category(name, photo_url):
  item = Category(
    category_label = name,
    photo = 'menu/' + photo_url
  )
  item.save()
  return item

def make_size(name, unit_label, amount, category):
  item = Size(
    size_label = name,
    unit_label = unit_label,
    amount = amount,
    category = category
  )
  item.save()
  return item

def make_product(name, category, ingredients):
  product = Product(
    product_label = name,
    category = category
  )
  product.save()
  for item in ingredients:
    make_ingredient(item, product)
  return product

def make_ingredient(name, product):
  item = Ingredient(
    ingredient_label = name,
    product = product
  )
  item.save()
  return item

def make_price(product, size, amount):
  item = Product(
    product = product,
    size = size,
    amount = amount,
    currency = '$'
  )
  item.save()
  return item

def make_categories():
  return AttrDict({
    'pizza': make_category('Pizza', 'pizza.jpg'),
    'pasta': make_category('Pasta', 'pasta.jpg'),
    'drinks': make_category('Drinks', 'drinks.jpg'),
    'salad': make_category('Salad', 'salad.jpg')
  })

def make_sizes(categories):
  return AttrDict({
    'small_pizza': make_size('Small', 'cm', 24, categories.pizza),
    'medium_pizza': make_size('Medium', 'cm', 30, categories.pizza),
    'large_pizza': make_size('Large', 'cm', 40, categories.pizza),
    'small_drink': make_size('300ml', 'ml', 300, categories.drinks),
    'big_drink': make_size('500ml', 'ml', 500, categories.drinks),
    'small_salad': make_size('Small', 'g', 200, categories.salad),
    'big_salad': make_size('Big', 'g', 500, categories.salad),
    'small_pasta': make_size('Small', 'g', 200, categories.pasta),
    'big_pasta': make_size('Big', 'g', 500, categories.pasta)
  })

def make_product_pizza(categories):
  return AttrDict({
    'margeritta': make_product('margeritta', categories.pizza, ['cheese', 'tomato sauce']),
    'vesuvio': make_product('vesuvio', categories.pizza, ['cheese', 'tomato sauce', 'ham']),
    'hawai': make_product('hawai', categories.pizza, ['cheese', 'tomato sauce', 'ham', 'pineapple']),
    'capriciosa': make_product('capriciossa', categories.pizza, ['cheese', 'tomato sauce', 'ham', 'mushrooms']),
    'kebab': make_product('kebab', categories.pizza, ['cheese', 'tomato sauce', 'kebab chicken']),
    'pepperoni': make_product('pepperoni', categories.pizza, ['cheese', 'tomato sauce', 'pepperoni']),
    'country': make_product('country', categories.pizza, ['cheese', 'tomato sauce', 'ham', 'mushrooms', 'bacon', 'onion'])
  })

def make_product_drink(categories):
  return AttrDict({
    'tea': make_product('tea', categories.drinks, []),
    'coffee': make_product('coffee', categories.drinks, []),
    'coca-cola': make_product('coca-cola', categories.drinks, []),
    'fanta': make_product('fanta', categories.drinks, []),
    'sprite': make_product('sprite', categories.drinks, []),
    'water': make_product('water', categories.drinks, []),
    'beer': make_product('beer', categories.drinks, [])
  })
  
def make_product_pasta(categories):
  return AttrDict({
    'bolognese': make_product('bolognese', categories.pasta, ['pasta', 'tomato sauce', 'pork meat']),
    'carbonara': make_product('carbonara', categories.pasta, ['pasta', 'bacon', 'eggs', 'cheese']),
    'vege': make_product('vege', categories.pasta, ['pasta', 'tomato', 'paprika', 'cabbage']),
    'pesto': make_product('pesto', categories.pasta, ['pasta', 'bazil', 'cheese'])
  })

def make_product_salad(categories):
  return AttrDict({
    'gyros': make_product('gyros', categories.salad, ['cabbage', 'chicken', 'onion', 'cucumber', 'tomato']),
    'vege': make_product('vege', categories.salad, ['cabbage', 'potato', 'onion', 'cucumber', 'tomato']),
    'cheese': make_product('cheese', categories.salad, ['cabbage', 'gouda', 'mascarpone', 'tofu']),
    'greece': make_product('greece', categories.salad, ['cabbage', 'feta cheese', 'black olives']),
  })

def make_products_all(categories):
  salad = make_product_salad(categories)
  pasta = make_product_pasta(categories)
  pizza = make_product_pizza(categories)
  drinks = make_product_drink(categories)

def make_menu():
  categories = make_categories()
  sizes = make_sizes(categories)
  make_products_all(categories)

def clear_all():
  Size.objects.all().delete()
  Price.objects.all().delete()
  Ingredient.objects.all().delete()
  Product.objects.all().delete()
  Category.objects.all().delete()

def init(clear = False):
  if clear:
    clear_all()
  if (Category.objects.all().count() == 0):
    make_menu()