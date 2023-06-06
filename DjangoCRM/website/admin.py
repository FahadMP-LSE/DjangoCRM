from django.contrib import admin

# Register your models here.

from .models import Record # to show database that we created in admin panel

admin.site.register(Record)