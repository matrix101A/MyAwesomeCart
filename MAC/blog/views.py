from django.shortcuts import render
from .models import Blogpost
from django.shortcuts import HttpResponse

def index(request):
    myposts=Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html',{'myposts':myposts})

def blogpost(request,id):
    blog=Blogpost.objects.filter(post_id=id)[0]
    print(blog)
    return render(request,'blog/blogpost.html',{'post':blog})
