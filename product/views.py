from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404

from .models import *
from .forms import *

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)



def Add_cart(request):
    user_id=request.session.get("id")
    user=request.user
    product_id=request.GET.get("prod_id")
    

    product=Product.objects.get(id=product_id)
    
    Cart(user=user,product=product).save()
    return redirect("/Pro-product")


def show_Cart(request):
     ids=request.session.get("id")

     obj=Cart.objects.filter(user=ids)
     amount=0
     for p in obj:
            
            value= p.quantity * p.product.price
            amount= value + amount
     total_amount= amount +50
  
     d={'data':obj,'total_amount':total_amount,'amount':amount}
     
     return render(request,'cart.html',d)
    
def delete(request,proid):
    obj=Cart.objects.get(id=proid)
    obj.delete()
    return redirect("/Pro-showcart")






def plus_cart(request,pid):
    if request.method=="GET":
        obj1=Cart.objects.get(id=pid)
   
        obj1.quantity +=1
        obj1.save()
    
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0

        for p in cart:
            
            value= p.quantity * p.product.price
            amount= value + amount
        total_amount= amount + 50
        data={
            "quantity":obj1.quantity,
            "amount":obj1.amount,
            "totalamount":obj1.total_amount,
            "price":value
        }
        return redirect("/Pro-showcart")

def minus_cart(request,pid):
    if request.method=="GET":
        c=Cart.objects.get(id=pid)
        c.quantity -=1
        c.save()
    
        user=request.user
        cart=Cart.objects.filter(user=user)
        if c.quantity==0:
            c.delete()
        amount=0    
        for p in cart:
            
            value= p.quantity *p.product.price
            amount= value + amount
        total_amount= amount + 50
        data={
            "quantity":c.quantity,
            "amount":c.amount,
            "totalamount":c.total_amount,
            "price":value
        }
        return redirect("/Pro-showcart")
    
def search(request):
  ids=request.session.get("id")

  srch=request.POST.get("srch")
  obj=Product.objects.filter(description__contains=srch)
  d={'products':obj}
  return render(request,'product_list.html',d) 

def order(request):
    ids=request.session.get("id")

    obj=Cart.objects.filter(user=ids)
    d={"data":obj}

    return render(request,"order.html",d)  


def address(request):
    
    return render (request,"address.html")


