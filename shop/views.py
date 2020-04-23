from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from . models import Product

# Create your views here.
def index(request):
      products = Product.objects.all()

      params = {'products': products}
      return render(request, 'shop/index.html', params)

def about(request):
      return render(request, 'shop/about.html')


def contact(request):
      return HttpResponse("we are at contact now")

def tracker(request):
      return HttpResponse("we are at tracker now")

def search(request):
      return HttpResponse("we are at search now")

def productview(request):
      products = Product.objects.all()
      return render(request, 'shop/productview.html', {'products': products})


def checkout(request):
      return HttpResponse("we are at checkout now")
