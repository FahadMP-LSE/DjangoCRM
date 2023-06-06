from django.db import models

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
  