from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username','city','address']

admin.site.register(User,UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','created_by']

admin.site.register(Post,PostAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['text','post','comment_by']

class EmpRegAdmin(admin.ModelAdmin):
    list_display = ['username','password','fullname','address','gender','city']

admin.site.register(EmpReg,EmpRegAdmin)