from django.shortcuts import render,redirect
from .models import Destination
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# Create your views here.

def index(request):
    item = Destination.objects.all()
    return render(request,"index.html",{'item': item})

def cart(request):
    item = Destination.objects.all()
    return render(request,"cart.html",{'item': item})

def aftlogin(request):
    if request.user.is_anonymous:
        return redirect("/login")
    item = Destination.objects.all()
    return render(request,"aftlogin.html",{'item': item})


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        print("done")
        print(user)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, "login.html")
        
    return render(request, "login.html")
    

def logoutuser(request):
    logout(request)
    return redirect("/login")

def signupusers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name,email,password)
        user.save()

    else:
        pass
    return render(request, "signup.html")