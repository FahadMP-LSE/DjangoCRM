from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages # to show messages e.g. logged in /logged out/registered successfully
from .forms import SignUpForm, AddRecordForm #importing form we created in forms.py file
from .models import Record, Profile


# Create your views here.

def home(request):#integrating login/logout here instead of in separate areas
    records= Record.objects.all()#grab all records



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
        return render(request,"home.html",{"records":records})#{} is an empty context dictionary
#"records": records above means that ifuser has logged in, should see all records.

def logout_user(request):
    logout(request)
    messages.success (request,"You have been logged out....")
    return redirect("home")

def register_user(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)#saying that whenever a form is filled, send to our SignUpForm
        if form.is_valid():#first checking if valid - django does this by itself
            form.save()#saving the SignUpForm
            #Authenticate and log in
            username=form.cleaned_data["username"]#form.cleaned gets the specific value from form "username" and assigns to username
            password=form.cleaned_data["password1"]
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered!!!")
            return redirect("home")
        
    else: # if not filling form but want to fill out fomr
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



        return render(request, "profile.html",{"profile":profile})
    else:
        messages.success(request,"There was an error logging in. Please Try again!")
        return redirect("home")
