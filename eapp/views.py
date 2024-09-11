from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import Contact ,Products,Placed_orders
from django.contrib.auth.models import User
from math import ceil
from django.contrib import messages
import json
import random


# Create your views here.

def index(request):
    # Query all products
    catprods = Products.objects.all()
    print(catprods,"pandi")
    allProds={}
    for i in catprods:
        if i.category not in allProds:
            allProds[i.category]=[]
            
        
        allProds[i.category].append(i)
    print(allProds,"siva")
    # Convert defaultdict to regular dictionary for template rendering
    
    # Pass grouped products to template
    return render(request, 'eapp/index.html', {'allProds': allProds})


def jsons(request):
    # Query all products
    catprods = Products.objects.all()
    print(catprods,"pandi")
    allProds={}
    for i in catprods:
        if i.category not in allProds:
            allProds[i.category]=[]    
        
        allProds[i.category].append({ 
            "product_Name":i.product_Name,
            "category": i.category,
            "subcatagory":i.subcatagory,
            "price":i.price,
            "desc" :i.desc,
            "images":i.images.url,
        })
    print(allProds,"siva")
    return JsonResponse(allProds)



def about(request):
    return render(request,'eapp/aboutus.html')


def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneNo=request.POST.get('phone')
        adress=request.POST.get('adress')
        help=request.POST.get('help')
        save= Contact(name=name,email=email,adress=adress,phoneNo=phoneNo,help=help)
        save.save()
        return redirect('contactus')
    return render(request,'eapp/contactus.html')

def requires(request):
    view=Contact.objects.all()
    return render(request,'eapp/requires.html',{'view':view})
    
def request_delete(request,id):
    delete=Contact.objects.get(id=id)
    delete.delete()
    return redirect('requires')


def checkout(selt):
    
    return render(selt,"checkout.html")


def order_history(self):
    num=random.randint(1, 100000)
    order_details={"data":[]}
    if self.method=="POST":
        data=json.loads(self.body)
        orders = data.get("order",[])
        
        for g in orders:
            name=g["name"]
            price=g["price"]
            qty=g["qty"]
            qty_total=g["tor_qty"]
            save=Placed_orders(order_id=num,product_name=name,product_qty=qty,product_total_price=qty_total,product_price=price)
            save.save()
               
        return  JsonResponse({"message":"data_sumitedsuccessfully"},status=200)
        
                
        
def order_placed(self):
    orders=Placed_orders.objects.all()
    print(orders)
    orderlist={}    
    for i in orders:
        if i.order_id not in orderlist :
            orderlist[i.order_id]=[]
    
        orderlist[i.order_id].append(i)
             
    return render(self,"eapp/orderhistory.html",{"send":orderlist})
            
            
        
    
             
    
    