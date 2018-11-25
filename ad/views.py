from django.shortcuts import render

def list(request):
  list = [] #Ad.objects.order_by('-pub_date')
  return render('ad/list.html', {
    'list': list
    'title': 'Announcements'
  })

def item(request, id):
  item = { 'title': 'texttexttext', 'text':'texttext'} #get_object_or_404(Ad, pk=id)
  return render('ad/item.html', {
    'item': item
  })

def latest(request):
  list = []#Ad.objects.order_by('-pub_date')[:5]
  return render('ad/list.html', {
    'list': list,
    'title': 'Latest announcements'
  })