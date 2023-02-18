# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required




@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
















@staff_member_required
def add_product(request):
    
    if request.method=="POST":
        Product_Name=request.POST.get('Product_Name')
        Product_Description=request.POST.get('Product_Description')    
        Specifications=request.POST.get('Specifications')    
        Stock=request.POST.get('Stock')    
        # product_stock=request.POST.get('product_stock')  
        print(Product_Name,Product_Description,Specifications,Stock)
        # image1=request.FILES["img1"]
        # image2=request.FILES["img2"]
        # image3=request.FILES["img3"]
        print("home view")
          
        object=AddProduct(product_name=Product_Name,product_description=Product_Description,product_specifications=Specifications,product_stock=Stock)
        print('1s')
        object.save()
        print('2s')
        # messages.success(request,"Product Added Successfully.")
        # messages.info(request, "product added successfully" )
        return redirect('add_product')
        
    return render(request, "home/add_product.html")



# ___________________________________________________________MY One ____________________________________________________________________________

