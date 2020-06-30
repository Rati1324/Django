from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import CreatePost,Comment_form
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def homepage(request):
    
    posts=Post.objects.all().order_by('date').reverse()
    # post_id=[str(i.id) for i in posts]

    # comments=[i.id_post for i in Comment.objects.all()]
    # comment_per_post=[comments.count(i) for i in post_id]
    
    # result=dict(zip(post_id,comment_per_post)) 
    return render(request,"homepage/homepage.html",{'posts':posts})
    # return HttpResponse((result[i],i) for i in result)

def post_details(request,post_id):
    
    details=Post.objects.all().get(id=post_id)
    
    form=Comment_form(request.POST)
    comments=Comment.objects.all().filter(id_post=post_id).order_by('date').reverse()
    
    if request.method=="POST":
   
        form=Comment_form(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.id_post=post_id
            num_of_comments=Post.objects.get(id=post_id)
            num_of_comments.comments_amount+=1
            num_of_comments.save()
            comment.save()
            
            return redirect(f"/{post_id}")
            
            
    else:
        form=Comment_form()
    return render(request,'homepage/post.html',{'details':details,'comments':comments,'form':form})


@login_required(login_url="/account/login/")
def create_post(request):
    if request.method=="POST":
        form=CreatePost(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            
        return redirect('/')
        
    else:
        form=CreatePost()
    return render(request,'homepage/create_post.html',{'form':form})


def search(request):
    keyword=request.GET['s']
    
    title=request.GET['s']
    results=Post.objects.all().filter(title__contains=keyword)
    
    return render(request,'homepage/homepage.html',{'posts':results,'title':title,'search':True})
    
    
    # return HttpResponse(title)
    
    
    

