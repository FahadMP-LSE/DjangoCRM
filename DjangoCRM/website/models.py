from django.db import models
from django.contrib.auth.models import User#we will extend user model to create user profiles
from django.db.models.signals import post_save# to automatically register new user profiles


# Create your models here.
#creating database model here...no need to know sql or any other thing..django does it itself.

#we make only in singular - django will do plural itslef..e.g. if we had made Records here, django will make it Recordss
class Record(models.Model):#django will change to records (plural)
    created_at=models.DateTimeField(auto_now_add=True)#timestamp automatically for when new record created
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=20)

    def __str__(self): #show what to show on screen when accessing records
        return(f"{self.first_name} {self.last_name}")
  

  #profiles for users
class Profile(models.Model):#importing model
    user=models.OneToOneField(User,on_delete=models.CASCADE) #associate one user to one profile
    #cascade means if delete a user delete profile too
    follows=models.ManyToManyField("self",
                                   related_name="followed_by",
                                   symmetrical=False,blank=True)#a user can follow many people
#symmetrical=False means one person can follow anotherbut the other person doesnt have to follow the first
#Blank=true means a person is not forced to follow someone

    date_modified=models.DateTimeField(User, auto_now=True)
    #adding profile image - note we are not saving user images but the links to the images
    profile_image=models.ImageField(null=True,blank=True,upload_to="images/")#null=true means if no pic, fine
#images/ will be in the media location we specified. e.g. media/images/...

    def __str__(self):
        return self.user.username#in profiles section, without this code, shows "profile object 1","profile object 2 etc..
    #we are now showing the actual usernames
    # 


#create profile when new user signs up...
def create_profile(sender,instance, created,**kwargs):
    if created:
        user_profile=Profile(user=instance)# send new user to our Profile#see above def pROFILE
        user_profile.save()
        #have user follow himself
        user_profile.follows.set([instance.profile.id])#want to follow the users own id...migration created it automatically for each user....see migration py files
        user_profile.save()

post_save.connect(create_profile,sender=User)

#create messaging/meep models

class Meep(models.Model):
    user=models.ForeignKey(User, related_name="meeps",
                           on_delete=models.DO_NOTHING)# make id for each key for records

    body=models.CharField(max_length=200,default="")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d %H:%M}):"
            f"{self.body}...."
            )


