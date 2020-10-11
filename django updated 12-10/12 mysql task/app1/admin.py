from app1.models import employees
from django.contrib import admin
from .models import employees, faculty,student

# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display =['name','address','company','city','salary']

class stuadmin(admin.ModelAdmin):
    list_display =['name','rollno','marks','subject']

class facultyadmin(admin.ModelAdmin):
    list_display =['name','department','specialisation','salary','just']

admin.site.register(employees,empadmin)
admin.site.register(student,stuadmin)
admin.site.register(faculty,facultyadmin)