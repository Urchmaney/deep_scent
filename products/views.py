# from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from products.models import Product

# Create your views here.
def index(request):
  json_data = serializers.serialize('json', Product.objects.all())
  return HttpResponse(json_data, content_type='application/json')