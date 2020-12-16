from django.shortcuts import render,HttpResponse,redirect
from .models import product
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

def home(request):

    if request.user.is_anonymous:
         return render(request,'login.html')
    else :
        return render(request,'Home.html')
    
    

def feature(request):
    return render(request,'feature.html')


def myprofile(request):
    if request.user.is_anonymous:
         return render(request,'login.html')
    else :
        return render(request,'myprofile.html')

    #return render(request,'myprofile.html')

def myorders(request):
    if request.user.is_anonymous:
         return render(request,'login.html')
    else :
        return render(request,'myorders.html')

    #return render(request,'myorders.html')

def logoutuser(request):
    logout(request)
    return redirect('Home.html')

def login1(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
             login(request,user)
             return redirect(request,'/')
        else:
             return redirect(request,'login.html')        


def signup(request):
   return render(request,'signup.html')
    