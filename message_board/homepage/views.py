from django.shortcuts import render,redirect
from post.models import Post
from django.http import HttpResponse


def homepage(request):
    
    posts=Post.objects.all().order_by('date').reverse()
    return render(request,"homepage/homepage.html",{'posts':posts})

def search(request):
    
    keyword=request.GET['s']
    title=request.GET['s']

    
    results_in_title=set(Post.objects.all().filter(title__contains=keyword))
    results_in_body=set(Post.objects.all().filter(body__contains=keyword))

    
    results=results_in_body.symmetric_difference(results_in_title)
    
    return render(request,'homepage/homepage.html',{'posts':results,'title':title,'search':True})
    
    
    

