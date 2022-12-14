from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import *


class Sign_in_user(LoginView):
    form_class = AuthenticationForm
    template_name = 'mysite/base.html'

def home(request):
    return render(request, 'mysite/home.html')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_Card_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'mysite/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_Card_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'mysite/checkout.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'mysite/store.html', context)
