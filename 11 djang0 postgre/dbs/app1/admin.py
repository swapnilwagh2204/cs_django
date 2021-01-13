from app1.models import employees
from django.contrib import admin
from .models import employees

# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display =['name','address','company','city','salary']

admin.site.register(employees,empadmin)