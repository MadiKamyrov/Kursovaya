from django.urls import path

from .views import *

urlpatterns = [
    path('', Sign_in_user.as_view(), name='base'),
    path('home/', home, name='home'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('store/', store, name='store'),
]