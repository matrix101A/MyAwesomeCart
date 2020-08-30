from django.shortcuts import render
from django.shortcuts import HttpResponse
from . models import product,Contact,Orders,OrderUpdate
import math,json
from datetime import  datetime
Products= product.objects.all()


def index(request):
    allProds=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods} #Gets all categories
    for cat in cats :
        prod=product.objects.filter(category=cat)
        n = len(prod)
        nSlides = int(n / 4 + math.ceil(n / 4 - n // 4))
        allProds.append([prod, range(1,nSlides), nSlides])

    params={'allProds':allProds}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=='POST':
        name= request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc= request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(request, 'shop/contact.html')

def tracker(request):

    if request.method == 'POST':
        OrderId = request.POST.get('OrderId', '')
        email = request.POST.get('email', '')
        try:
            order=Orders.objects.filter(order_id=OrderId,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=OrderId)
                updates=[]
                for item in update:
                     updates.append({'text':item.update_desc,'time':item.timestamp})
                     response= json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else :
                return  HttpResponse('{}')
        except Exception as e:
            return  HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request,'shop/search.html')

def productView(request,myid):
    #fetch product using id
    Product = product.objects.filter(id=myid)
    return render(request,'shop/prodView.html',{'product':Product[0]})

def checkout(request):
    if request.method=='POST':
        name= request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        city= request.POST.get('city','')
        state= request.POST.get('state','')
        zip_code= request.POST.get('zip_code','')
        address= request.POST.get('address1','')+request.POST.get('address2','')
        items_json=request.POST.get('itemsjson','')
        order=Orders(name=name,email=email,phone=phone,city=city,state=state,zip_code=zip_code,address=address,
                     items_json=items_json)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="Your order has been placed !")
        update.save()
        id=order.order_id
        thank = True
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')
