from django.contrib import admin

# Register your models here.
from .models import Student, Employee, Post


class StudentAdmin(admin.ModelAdmin):

    list_display = ['rollno','name','marks']

admin.site.register(Student,StudentAdmin)


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['username','password','name']

admin.site.register(Employee,EmployeeAdmin)


class PostAdmin(admin.ModelAdmin):

    list_display = ['title','cover']

admin.site.register(Post,PostAdmin)