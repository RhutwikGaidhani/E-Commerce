# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
import datetime
import os

from django.contrib.admin.views.decorators import staff_member_required

# from ..apps.models import AddProduct

# Create your models here.
# class AdminLoginForm(models.Model):
#     username=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)

# ________________________________________________________________MY ONE ________________________________________________________________


def filepath(request, filename):
    old_filename = filename
    timeNow=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s",(timeNow, old_filename)
    return os.path.join('uploads/', filename)

class AddProduct(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    product_description=models.TextField()
    product_specifications=models.TextField()
    product_stock=models.IntegerField()
    # Image1=models.ImageField(upload_to='profile_pic1')
    # Image2=models.ImageField(upload_to='profile_pic2')
    # Image3=models.ImageField(upload_to='profile_pic3')
    product_image=models.ImageField(upload_to='filepath', null=True, blank=True)


class Cart(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    usercart=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    quantity=models.IntegerField()


class profile(models.Model):
    username=models.CharField(max_length=50)
    emailid=models.EmailField()
    address=models.CharField(max_length=100)
    phone_number=models.IntegerField(null=None,blank=True)
    profile_img=models.ImageField(upload_to='profile',null=True, blank=True)
def profile1(request):
    old_filename = filename
    timeNow=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s",(timeNow, old_filename)
    return os.path.join('uploads/', filename)
    


    
    