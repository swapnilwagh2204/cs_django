
from django.contrib import admin
from .models import student

# Register your models here.


class stuadmin(admin.ModelAdmin):
    list_display =['name','rn','marks']
    