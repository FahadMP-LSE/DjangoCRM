from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages # to show messages e.g. logged in /logged out/registered successfully

# Create your views here.

def home(request):#integrating login/logout here instead of in separate areas
#check to see if logging in (posting) otherwise (getting request)
    if request.method=="POST":
        username=request.POST["username"]#saying that get their username (for placeholder Username)
        password=request.POST["password"]
        #running logic - authenticate

        user=authenticate(request,username=username,password=password)#authenticate is function which takes arguments
        if user is not None:
            login(request,user)
            #if username and password correct, logged in
            messages.success(request, "You have been logged in!")
            return redirect("home")
        else:
            messages.success(request,"There was an error logging in. Please Try again!")
            return redirect("home")
    else:         
        return render(request,"home.html",{})#{} is an empty context dictionary

def logout_user(request):
    logout(request)
    messages.success (request,"You have been logged out....")
    return redirect("home")

def register_user(request):
    return render(request,"register.html",{})#{}
