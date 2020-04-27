from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import  render, get_object_or_404
from . models import Product
from . models import Contact

# Create your views here.
def index(request):
      products = Product.objects.all()

      params = {'products': products}
      return render(request, 'shop/index.html', params)

def about(request):
      return render(request, 'shop/about.html')


def contact(request):
      contacts = Contact.objects.all()
      return render(request, 'shop/contact.html', {'contacts': contacts})



def tracker(request):
      return HttpResponse("we are at tracker now")

def productdetail(request, product_id):
      product = get_object_or_404( Product, pk=product_id)
      return render(request, 'shop/productdetail.html',{'product':product})

def productview(request):

      products = Product.objects.all()
      return render(request, 'shop/productview.html', {'products': products})


def checkout(request):
      return render(request, 'shop/checkout.html')
