from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import Http404, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
import json

from base.utils import render
from .models import Contact, Message

def index(request):
  try:
    contact = Contact.objects.all()[:1].get()
    gmap = (contact.latitude and contact.longitude)
    return render(request, 'contact/index.html', {
      'contact': contact,
      'gmap': gmap
    })
  except ObjectDoesNotExist:
    return render(request, 'contact/index.html')

def postMessage(request):
  POST = json.loads(request.body)
  msg = Message(
    subject = POST['subject'],
    email = POST['email'],
    message = POST['message']
  )
  msg.save()
  return JsonResponse({
    'success':'true'
  })