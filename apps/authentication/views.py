# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from ast import Pass
from asyncio.windows_events import NULL
from cProfile import Profile
from email import message
from genericpath import exists
from itertools import product
from multiprocessing import context
from pickle import NONE
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm,AdminLoginForm
from .models import *
from django.contrib.auth.models import User,auth
# from apps.home import models
from apps.home.models import AddProduct,Cart,profile
import os
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User





def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            superusers = User.objects.get(is_superuser=True)
            print(user)
            print(username)
            
            # superusers_username = User.objects.filter(is_superuser=True).values('username')
           
            print(superusers)
            # print(User.is_superuser)
            # if user is not None:
            #         print("none wala")
            #         login(request, user)
            #         return redirect("/")
            # else:
            #     msg = 'Invalid credentials'
            
            if user==superusers:
                print("admin1")
                form=AdminLoginForm()
                print("admin2")
                login(request, user)
                return render(request,"home/add_product.html")
            else:
                if user is not None:
                    print("none wala")
                    login(request, user)
                    return render(request,"home/start.html")
                else:
                    msg = 'Invalid credentials'
        else:
            # if request.user.is_superuser== True:
            #     print("admin1")
            #     form=AdminLoginForm(instance=request.user)
            #     print("admin2")
            # else:
            #     print("user1")
            #     form=LoginForm(instance=request.user)
            #     print("user2")


            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created '
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})




# _________________________________________________MY One_________________________________________________________________

def forgetpassword(request):
    msg = None
    success = False
    if request.method == "POST":
        username=request.POST.get('username')
        print(username)
        Newpassword=request.POST.get('newpassword')
        Conformpassword=request.POST.get('conformpassword')
        user = None
        print(user)
        if Newpassword==Conformpassword:
            try:
                user=User.objects.get(username=username)
            except:
                pass
            print(user)
            if user is not None:
                print("fdfhsdjfhjdhffskhkh")
                u=User.objects.get(username=username)
                u.set_password(Newpassword)
                u.save()
                msg='change succesfull'
                return redirect('login')
            msg= 'User not found'
            print("dkfhdsjfhdksjfhk")
            pass
        else:
            msg= 'Password Not Matched'
    return render(request, 'accounts/forgetpassword.html',{"msg": msg, "success": success})
    # return render(request, 'accounts/changepassword.html')

def changepassword(request):
    msg = None
    success = False
    if request.method=='POST':
        new_pass=request.POST.get("newpassword")
        conformpassword=request.POST.get("conformpassword")
        print(new_pass)
        print(conformpassword)
        user=request.user
        print(user)
        if new_pass==conformpassword:
            u=User.objects.get(username=user.username)
            u.set_password(new_pass)
            u.save()
            msg='change succesfull'
            print(new_pass)
            return redirect('/')
        # return render(request,'accounts/changepassword',{'msg':msg,'success':success})
        else:
            msg='password not matched'
    return render(request,'accounts/changepassword.html',{"msg": msg, "success": success})






# def AdminLoginForm(request):
#     form = AdminLoginForm(request.POST or None)

#     msg = None

#     if request.method == "POST":

#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             AdminLoginForm = authenticate(username=username, password=password)
#             if AdminLoginForm is not None:
#                 login(request, AdminLoginForm)
#                 return redirect("/")
#             else:
#                 msg = 'Invalid credentials'
#         else:
#             msg = 'Error validating the form'

#     return render(request, "accounts/login.html", {"form": form, "msg": msg})
#     return render(request, "AdminLoginForm.html")



@staff_member_required
def add_product(request):
    return render(request,'home/add_product.htmlS')

@staff_member_required
def add_product(request):
    if request.method=="POST":
        
        object=AddProduct()
        product_name=request.POST.get('Product_Name')
        product_description=request.POST.get('Product_Description')    
        product_specifications=request.POST.get('Specifications')    
        product_stock=request.POST.get('Stock')    
        product_price=request.POST.get('Price')  

        if len(request.FILES) != 0:
            product_image=request.FILES['img[]']

        print(product_name,product_description,product_specifications,product_stock,product_price)
        # image1=request.FILES["img1"]
        # image2=request.FILES["img2"]
        # image3=request.FILES["img3"]
        print("app view")
          
        object=AddProduct(product_name=product_name,product_description=product_description,product_specifications=product_specifications,product_stock=product_stock,product_price=product_price,product_image=product_image)
        
        print('1s')
        object.save()
        print('2s')
        # messages.success(request,"Product Added Successfully.")
        # messages.info(request, "product added successfully" )
        return redirect('add_product')
        
    return render(request, "home/add_product.html")


@staff_member_required
def product_list(request):
    print('1')
    product_list=AddProduct.objects.all()
    print(product_list)
    print('2')
    context={'product_list':product_list}
    print('3')
    return render(request,"home/product_list.html",context)
@staff_member_required
def delete(request, id):
    print('del1')
    product=AddProduct.objects.get(id=id)
    print('del12')

    product.delete()
    print('del13')

    # messages.success(request,"Product deleted Successfully.")
    return redirect("product_list")


# def update_product2(request, id):
#     prod= AddProduct.objects.get(id=id)
#     context ={'prod':prod}
#     return render(request,'home/update_product.html',context)

@staff_member_required
def update_product(request, id):
    prod= AddProduct.objects.get(id=id)
    if request.method == "POST":

        if len(request.FILES) != 0:
            if len(prod.product_image) >0:
                os.remove(prod.product_image.path)
            prod.product_image= request.FILES['img[]']

        prod.product_name=request.POST.get('Product_Name')
        prod.product_description=request.POST.get('Product_Description')
        prod.product_specifications=request.POST.get('Specifications')
        prod.product_stock=request.POST.get('Stock')
        prod.product_price=request.POST.get('Price')
        prod.save()
        # messages.success(request, "Prouduct Updated Successfully")
        return redirect('product_list')

    context ={'prod':prod}
    return render(request,'home/update_product.html',context)


@staff_member_required
def orders(request):
    orders=Cart.objects.all()
    stock=AddProduct.objects.all()
    context={'orders':orders,'stock':stock}
    
    return render(request,'home/orders.html',context)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++   USER  +++++++++++++++++++++++++++++++++++++++++++++
def explore(request):
    product_list=AddProduct.objects.all()
    print(product_list)
    print('55')
    context={'product_list':product_list}
    print('6')
    
    return render(request,'home/explore.html',context)


def cart(request,id):
    if request.method=="POST":
        product= AddProduct.objects.get(id=id)
        # print(product.product_name)
        user=request.user
        user2=user.id
        print(user2)
        prod=Cart()
        product_name=product.product_name
        product_price=product.product_price
        # print(User.get_username)
        # prod=Cart(product_name=product_name,product_price=product_price,usercart=user)
        # prod.save()
        # print(prod)
        prod2=Cart.objects.filter(usercart=user2,product_name=product_name)
        prod3=Cart.objects.filter(product_name=product_name)
        print(User.get_username)
        # if not prod2:
        #     if not prod3:
        #         quantity=1
        #         prod=Cart(product_name=product_name,product_price=product_price,usercart=user,quantity=quantity)
        #         prod.save()
        print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
        print(prod2)
        print(user2)
        print(product_name)

        print(len(prod2))
        print(len(prod3))

        if len(prod2)>0:
            if len(prod3)>0:
                prod4= Cart.objects.get(usercart=user2,product_name=product_name)
                if prod4:
                    quantity=prod4.quantity
                    quantity=quantity+1
                    print(quantity)
                    prod4.quantity=quantity
                    # print(prod.quantity)
                    # prod=Cart(quantity=quantity)
                    prod4.save()
            else:
                quantity=1
                prod=Cart(product_name=product_name,product_price=product_price,usercart=user,quantity=quantity)
                prod.save()
        else:
                quantity=1
                prod=Cart(product_name=product_name,product_price=product_price,usercart=user,quantity=quantity)
                prod.save()
        

        # __________stock decrease_______
        c= AddProduct.objects.get(id=id)
        c.product_stock=c.product_stock - 1 
        if c.product_stock > 0:
            c.save()
        else:
            c.product_stock=0
            c.save()

        # _______end_______

        
        return redirect('explore')


def showcart(request):
    user=request.user
    user2=user.id
    product_list= Cart.objects.filter(usercart=user2)
    print(product_list)
    context={'product_list':product_list}
    # print('31')
    return render(request,'home/showcart.html',context)


def remove(request, id):
    print('del1')
    # ________________________________restore stock_________________
    product=Cart.objects.get(id=id)
    restore=product.quantity
    name=product.product_name
    name1=AddProduct.objects.get(product_name=name)
    # name2=name1.product_stock
    name1.product_stock=name1.product_stock+product.quantity
    name1.save()
    # name2=name1.product_stock
    print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    print(restore)
    print(name1)
    # print(name2)
    
    # _____________delete___________
    print('del12')

    product.delete()
    print('del13')

    


    # messages.success(request,"Product deleted Successfully.")
    return redirect("showcart")
# def restore(request,id):
#     if request.method == "POST":
#         res=request.POST.get('product_list.quantity')
#         print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
#         print(res)
#         return redirect("showcart")


# _____________________________________________________common i.e. profile_____________________
def rofile(request):
    user=request.user
    try:
        profil2=profile.objects.get(username=user.username)
        print(profil2,"rrrrrr")
        context={'user':user,'profil2':profil2}
        return render(request,'home/profile.html',context)
    except:
        return render(request,'home/profile.html')


def rofile1(request):
    user=request.user
    if request.method=="POST":
        profil=profile()
        profil1=profile.objects.filter(username=user.username)
        if len(profil1)>0:
            profil2=profile.objects.get(username=user.username)
            profil2.username=request.POST.get('username')
            profil2.emailid=request.POST.get('email')
            profil2.address=request.POST.get('address')
            # _______________________username logic_________________
            print(profil2.username)
            print(user.username)
            if profil2.username==user.username:
                pass
            else:
                user.username=request.POST.get('username')
                print(user.username)
                user.save()
            if profil2.emailid==user.email:
                pass
            else:
                user.email=request.POST.get('email')
                user.save()
            # _______________________address and number logic___________
            if profil2.address=="":
                profil2.address=NONE
            else:
                pass
            profil2.phone_number=request.POST.get('phone_number')
            if profil2.phone_number=="":
                profil2.phone_number=000000000
            else:
                pass
            # __________________________end logic_______________________
            # ________________________________img logic_______________________
            if len(request.FILES) != 0:
                print('if len')
                # os.remove(prod.product_image.path)
                profil2.profile_img=request.FILES['profile']
            else:
                print('eeeeeeeeeeeellllllllllllssssssssssseeeeeeeeeeeeeeee')
            # _______________________end logic____________________
            # profile_img=NULL
            print(user.username)
            print(profil2.username)  
            if user.username==profil2.username:
                pass
            context={'user':user,'profil2':profil2}

            profil2.save()
        else:
            print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
            username=request.POST.get('username')
            emailid=request.POST.get('email')
            address=request.POST.get('address')
            phone_number=request.POST.get('phone_number')
            if phone_number=="":
                phone_number=00000000000
                print('ssssssssssssssssssssssssss')
            else:
                pass
            # profile_img=NULL
            print(profil.username)
            if len(request.FILES) != 0:
                print('if len')
                # os.remove(prod.product_image.path)
                profile_img=request.FILES['profile']
            else:
                print('eeeeeeeeeeeellllllllllllssssssssssseeeeeeeeeeeeeeee')
                profile_img=None
            # profil(username=username,emailid=emailid,address=address,phone_number=phone_number,profile_img=profile_img)
            profil=profile(username=username,emailid=emailid,address=address,phone_number=phone_number,profile_img=profile_img)
            profil.save()
            context={'user':user,'profil':profil}
        try:
            context={'user':user,'profil2':profil2}
        except:
            context={'user':user}
        return render(request,'home/profile.html',context)
    return render(request,'home/profile.html')


