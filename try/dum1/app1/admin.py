
from django.contrib import admin
from .models import student,studentinfo,manufact,manufactinfo,users,commnunity

# Register your models here.


class studentadmin(admin.ModelAdmin):
    list_display =['name','rollno','marks','subject']
# admin.site.unregister(student)
admin.site.register(student,studentadmin)


class studentinfoadmin(admin.ModelAdmin):
    list_display =['student','mob','city','pincode']

admin.site.register(studentinfo,studentinfoadmin)


class manufactadmin(admin.ModelAdmin):
    list_display =['comp_name','manuf','origin_country']

admin.site.register(manufact,manufactadmin)


class manufactinfoadmin(admin.ModelAdmin):
    list_display =['manufact','carname','price','trans','eng']

admin.site.register(manufactinfo,manufactinfoadmin)

class useradmin(admin.ModelAdmin):
    list_display =['username','exp']
admin.site.register(users,useradmin)

class userinfoadmin(admin.ModelAdmin):
    list_display =['community_name','popularity']
admin.site.register(commnunity,userinfoadmin)

