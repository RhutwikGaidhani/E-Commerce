# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from os import stat
from django.urls import path
from .views import  explore, login_view, register_user,add_product,product_list,delete,update_product,cart,showcart,remove,orders,changepassword,rofile,forgetpassword,rofile1
from django.contrib.auth.views import LogoutView


# __________________my imports_____________
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', login_view, name="login"),

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),


    # __________________________________________________________my one______________________________________________
    
    # path('AdminLoginForm/', AdminLoginForm, name="AdminLoginForm"),
    # path('changepassword',changepassword, name='changepassword'),

    path('add_product',add_product, name='add_product'),
    # path('add_product1',add_product1, name='add_product1'),

    # path('',product_list, name='product_list'),
    path('product_list',product_list, name='product_list'),
    path('delete/<int:id>',delete ,name='delete'),
    path('delete/<int:id>',delete ,name='delete'),
    path('update_product/<int:id>',update_product ,name='update_product'),
    path('explore',explore, name='explore'),
    path('cart/<int:id>',cart, name='cart'),
    path('showcart',showcart, name='showcart'),
    path('remove/<int:id>',remove ,name='remove'),
    path('orders',orders ,name='orders'),
    path('changepassword',changepassword ,name='changepassword'),
    path('forgetpassword',forgetpassword ,name='forgetpassword'),
    path('profile',rofile ,name='profile'),
    path('profile1',rofile1 ,name='profile1'),
    

    # path('restore/<int:id>',restore ,name='restore'),








]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



