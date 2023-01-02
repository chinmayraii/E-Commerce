from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.http import JsonResponse
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




 
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

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        item_already_in_cart=False
        if request.user.is_authenticated:
            item_already_in_cart=Cart.objects.filter(Q(product=product.id)& Q(user=request.user)).exists()
            return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})
        else:
            return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})


def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    return render(request,('app/addtocart.html'))

def product_detail(request):
 return render(request, 'app/productdetail.html')

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
