from django.shortcuts import render
from .  models import category,Product
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
def allprodcat(request):
    c=category.objects.all()
    return render(request,'category.html',{'c':c})

def allproduct(request,p):
    c=category.objects.get(slug=p)
    p=Product.objects.filter(category__slug=p)
    return render(request,'product.html',{'p':p,'c':c})


def details(request,l):
    l=Product.objects.get(slug=l)
    return render(request,'details.html',{'l':l})

def signup(request):
    if(request.method=='POST'):
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        s=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        s.save()
        return user_login (request)
    return render(request,'signup.html')

def user_login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return allprodcat(request)
        else:
            messages.error(request,'Invalid user')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return allprodcat(request)

