from django.contrib import admin
from django.contrib.auth.models import Group# this is groups in admin panel

from django.contrib.auth.models import User# this is user in django admin panel
from .models import Profile,Meep# we created Profile in models.py - registering ehre
# Register your models here.

from .models import Record # to show database that we created in admin panel

admin.site.register(Record)


#Removing groups from database

admin.site.unregister(Group)

# #in admin panel, both profile and users appear as separate tables...want to merge these)

class ProfileInLine(admin.StackedInline):
    model=Profile

#Removing some unwanted features like email id, first last name etc

class UserAdmin(admin.ModelAdmin): # inheriting the class
    model=User
    #Just display username fields
    fields=["username"]
    inlines=[ProfileInLine]
    #we first need to unregister initial user and then re-register


admin.site.unregister(User)#unregister
#re register User
admin.site.register(User, UserAdmin)#user and useradmin registered

#admin.site.register(Profile)
admin.site.register(Meep)                
                    
#admin.site.unregister(Meep)#unregister
