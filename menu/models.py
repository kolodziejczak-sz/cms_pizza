from django.db import models


category
  -id
  -category_label

size:
  -id
  -category_id
  -size_label

product:
  -id
  -category_id
  -product_label

ingredient:
  -id
  -product_id

price:
  -id
  -product_id
  -size_id
  -amount,
  -currency
