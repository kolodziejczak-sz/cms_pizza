from django.shortcuts import render
from datetime import datetime 

def index(request):
  return render(request, 'base/index.html', {
    'title': 'test'
  })
  
def subsite(request):
  item = {
    'title': 'Artykuł',
    'image': 'https://i0.wp.com/paristech.com/wp-content/uploads/2013/09/header-b88d930b520c523ef8a53abfb86d75231.png',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'pub_date':  datetime.now()
  }
  return render(request, 'base/subsite.html', {
    'item': item
  })