from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import CreatePost,Comment_form
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

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
            
            return redirect(f"/post/{post_id}")
            
            
    else:
        form=Comment_form()
    return render(request,'post/post.html',{'details':details,'comments':comments,'form':form})


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
    return render(request,'post/create_post.html',{'form':form})


    
@login_required(login_url="/account/login/")    
def delete_post(request,post_id):
    
    the_post = Post.objects.all().filter(id=post_id)
    post_author_id=the_post[0].author_id
    
    post_author_name=User.objects.all().filter(id=post_author_id)
    post_author_name=post_author_name[0].username
    
    if request.user.username == post_author_name:
        
        the_post=Post.objects.all().filter(id=post_id)
        the_post.delete()
    return redirect('/')

@login_required(login_url="/account/login/") 
def edit_post(request,post_id):
    the_post = Post.objects.all().filter(id=post_id)
    post_author_id=the_post[0].author_id
    
    post_author_name=User.objects.all().filter(id=post_author_id)
    post_author_name=post_author_name[0].username
    
    if request.user.username == post_author_name:
        form=CreatePost()
        post=Post.objects.all().filter(id=post_id)[0]
        title=post.title
        body=post.body
        
        if request.method=='GET':
            
            return render(request,'post/edit_post.html',{'form':form,'title':title,'body':body})
        else:
            the_post=the_post[0]
            the_post.body=request.POST.get('body',False)
            the_post.title=request.POST.get('title',False)
            the_post.save()            
            
            return redirect(f'/post/{post_id}')