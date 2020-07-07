from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
    	 form = RegisterForm(request.POST)
    	 if form.is_valid():
             user=form.save()
             login(request,user)
             return redirect('/')
    else:
        form = RegisterForm()
 
    return render(request, "account/register.html", {"form":form})

def login_view(request):
    if request.method=="POST":
        
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('/')
        
    else:
        form=AuthenticationForm()
        
    return render(request,"account/login.html",{'form':form})

def logout_view(request): 
    if request.method=="POST":
        logout(request)
        return redirect('/')
    
    
    
    
    
    
    
    