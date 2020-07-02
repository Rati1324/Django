from django.shortcuts import render,redirect


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from post.models import Post

def homepage(request):
    
    posts=Post.objects.all().order_by('date').reverse()
    # post_id=[str(i.id) for i in posts]

    # comments=[i.id_post for i in Comment.objects.all()]
    # comment_per_post=[comments.count(i) for i in post_id]
    
    # result=dict(zip(post_id,comment_per_post)) 
    return render(request,"homepage/homepage.html",{'posts':posts})
    # return HttpResponse((result[i],i) for i in result)




def search(request):
    keyword=request.GET['s']
    
    title=request.GET['s']
    results=Post.objects.all().filter(title__contains=keyword)
    
    return render(request,'homepage/homepage.html',{'posts':results,'title':title,'search':True})
    
    
    # return HttpResponse(title)
    
    
    

