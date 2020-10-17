from django.contrib import admin
from .models import *
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ['id','tag_name']

admin.site.register(Tag,TagAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','created_by']

admin.site.register(Post,PostAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['text','post','comment_by']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['username','password','name']

admin.site.register(Employee,EmployeeAdmin)

