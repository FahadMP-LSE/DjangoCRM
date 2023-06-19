from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages # to show messages e.g. logged in /logged out/registered successfully
from .forms import SignUpForm, AddRecordForm,MeepForm,ProfilePicForm #importing form we created in forms.py file
from .models import Record, Profile,Meep
from django.contrib.auth.forms import UserCreationForm#may not need this
from django import forms# may not need this
from django.contrib.auth.models import User

# Create your views here.

def home(request):#integrating login/logout here instead of in separate areas
    if request.user.is_authenticated:#show meeps to people logged in
        form=MeepForm(request.POST or None)#form to post meeps
        if request.method=="POST":
            if form.is_valid():
                meep=form.save(commit=False)#not saving just now
                meep.user=request.user# saying whoever is logged in is meep user and save his work
                meep.save()
                messages.success(request,("Your message is posted successfully!"))
                return redirect("home")
        
        meeps=Meep.objects.all().order_by("-created_at")#reversing order to show latest meeps first otherwise shows oldest meeps first
        return render(request,"home.html",{"meeps":meeps,"form":form})
    else:
        meeps=Meep.objects.all().order_by("-created_at")
        return render(request,"home.html",{"meeps":meeps})
    



# #check to see if logging in (posting) otherwise (getting request)
#     if request.method=="POST":
#         username=request.POST["username"]#saying that get their username (for placeholder Username)
#         password=request.POST["password"]
#         #running logic - authenticate

#         user=authenticate(request,username=username,password=password)#authenticate is function which takes arguments
#         if user is not None:
#             login(request,user)
#             #if username and password correct, logged in
#             messages.success(request, "You have been logged in!")
#             return redirect("home")
#         else:
#             messages.success(request,"There was an error logging in. Please Try again!")
#             return redirect("home")
#     else:         
#         return render(request,"home.html",{"records":records})#{} is an empty context dictionary
# #"records": records above means that ifuser has logged in, should see all records.

def logout_user(request):
    logout(request)
    messages.success (request,"You have been logged out....")
    return redirect("home")

def login_user(request):
    if request.method=="POST":# if filling form and not only browsing website
        username=request.POST["username"]
        password=request.POST["password"]

        #need to see which user trying to login
        user=authenticate(request,username=username,password=password)
        if user is not None:#if actual user
            login(request, user)#log user in
            messages.success(request,("You are logged in! Enjoy!"))
            return render(request,"home.html")

    else:    
        messages.success(request,("There was an error logging in. Please try again!"))
        return render(request,"login.html",{})


def register_user(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)#saying that whenever a form is filled, send to our SignUpForm
        if form.is_valid():#first checking if valid - django does this by itself
            form.save()#saving the SignUpForm
            #Authenticate and log in
            username=form.cleaned_data["username"]#form.cleaned gets the specific value from form "username" and assigns to username
            password=form.cleaned_data["password1"]
            # first_name=form.cleaned_data["first_name"]
            # last_name=form.cleaned_data["last_name"]
            # email=form.cleaned_data["email"]
            #log in user
            user=authenticate(username=username,password=password)#if need first_name,last_name and email for authenticiation, uncomment above
            login(request,user)
            messages.success(request,"You have successfully registered!!!")
            return redirect("home")
        
    else: # if not filling form but want to fill out form
        form=SignUpForm()#need to pass form to the page
    return render(request,"register.html",{"form":form})#{} to pass form to the page using context dictionary


    #return render(request,"register.html",{"form":form})#{} to pass form to the page using context dictionary

def customer_record(request, pk):#pk is the primary key -ID of record e.g. 1 or 2
    if request.user.is_authenticated:
        #look up records if customer logged in
        customer_record=Record.objects.get(id=pk)
        return render(request,"record.html",{"customer_record":customer_record})
    else:
        messages.success(request,"You must be logged in to view records!")
        return redirect("home")

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"message deleted successfully!")
        return redirect("home")
    else:
        messages.success(request,"You must be logged in to view records!")
        return redirect("home")

def add_record(request):
    form=AddRecordForm(request.POST or None)#are they posting a form? if not, go to webpage
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record added!")
                return redirect("home")
        return render(request,"add_record.html",{"form":form})

    else:
         messages.success(request,"You must be logged in to add records!")
         return redirect("home")
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None, instance=current_record)#sending an instance of the form back to the page.
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated!")
            return redirect("home")
        return render(request,"update_record.html",{"form":form})
    else:
        messages.success(request,"You must be logged in to add records!")
        return redirect("home")
    

def profile_list(request):
    if request.user.is_authenticated:
        profiles=Profile.objects.exclude(user=request.user)# want to show profiles but do not want to see our own profile
        return render(request,"profile_list.html",{"profiles":profiles})
    else:
        messages.success(request, "You must be logged in to view this page")
        return render("home")
        
def view_records(request):
    if request.user.is_authenticated:
        records= Record.objects.all()#grab all records
        return render(request,"view_records.html",{"records":records})
    else:
        messages.success(request, "You must be logged in to view this page")
        return render(request,"home.html")

# #check to see if logging in (posting) otherwise (getting request)
#     if request.method=="POST":
#         username=request.POST["username"]#saying that get their username (for placeholder Username)
#         password=request.POST["password"]
#         #running logic - authenticate

#         user=authenticate(request,username=username,password=password)#authenticate is function which takes arguments
#         if user is not None:
#             login(request,user)
#             #if username and password correct, logged in
#             messages.success(request, "You have been logged in!")
#             return redirect("home")
#         else:
#             messages.success(request,"There was an error logging in. Please Try again!")
#             return redirect("home")
#     else:         
   # return render(request,"view_records.html",{"records":records})#{} is an empty context dictionary
#"records": records above means that ifuser has logged in, should see all records.


def profile(request, pk):
    if request.user.is_authenticated:
        profile=Profile.objects.get(user_id=pk)
        meeps=Meep.objects.filter(user_id=pk).order_by("-created_at")

        #Post form logic for follow/unfollow button
        if request.method=="POST":
            #get current user id
            current_user_profile=request.user.profile
            #get form data
            action=request.POST["follow"] #name for follow/unfollow button is follow
            #decide to follow/unfollow
            if action=="unfollow":
                current_user_profile.follows.remove(profile) # profile is primary key of page we are on
            elif action=="follow":#can use else too
                current_user_profile.follows.add(profile)
                #save the profile 
            current_user_profile.save()



        return render(request, "profile.html",{"profile":profile,"meeps":meeps})
    else:
        messages.success(request,"There was an error logging in. Please Try again!")
        return redirect("home")


def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)#getting id of current user
        profile_user=Profile.objects.get(user__id=request.user.id)#grab profile of current loggd in users.
        #get forms
        
        user_form=SignUpForm(request.POST or None,request.FILES or None,instance=current_user)#passing all info of curent user to the page so that it is displayed and user can change it.
        profile_form=ProfilePicForm(request.POST or None,request.FILES or None,instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()


            login(request,current_user)# making sure it relogs us in.
            messages.success(request,("Your message is updated successfully!"))
            return redirect("home")
        
        return render(request, "update_user.html",{"user_form":user_form,"profile_form":profile_form})

    else:
        messages.success(request,"You must be logged in")
        return redirect("home")
        
def meep_like(request, pk):
    if request.user.is_authenticated:
        meep=get_object_or_404(Meep,id=pk)#object to query something from the database and return error if there is a priblem
    #getting meep that matches id...next is logic
        if meep.likes.filter(id=request.user.id):
            meep.likes.remove(request.user)
        else:
            meep.likes.add(request.user)
     
        return redirect (request.META.get("HTTP_REFERER"))#REDIRECTS to the page that referrred us

    else:
        messages.success(request,("You must be logged in"))
        return redirect("home")