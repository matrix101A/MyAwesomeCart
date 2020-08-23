from django.shortcuts import render
from django.shortcuts import HttpResponse
from . models import product
import math
Products= product.objects.all()
print(Products)

def index(request):

    #n=len(Products)
    #nSlides=int(n/4+math.ceil(n/4-n//4))

    #allProds=[[Products,range(1,nSlides),nSlides],[Products,range(1,nSlides),nSlides]]
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
    return HttpResponse("We are at contact")
def tracker(request):
    return HttpResponse("We are at tracker")
def search(request):
    return HttpResponse("We are at search")
def productView(request):
    return HttpResponse("We are at product view")
def checkout(request):
    return HttpResponse("We are at checkout")