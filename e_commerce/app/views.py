from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.http import JsonResponse
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required




 
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears= Product.objects.filter(category='BW')
        mobiles= Product.objects.filter(category='M')
        laptops= Product.objects.filter(category='L')
        return render(request, 'app/home.html',
        {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles': mobiles,"laptops":laptops})

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')


def login(request):
 return render(request, 'app/login.html')

@login_required
def registration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
