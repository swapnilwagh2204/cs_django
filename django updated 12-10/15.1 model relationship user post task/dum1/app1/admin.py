
from django.contrib import admin
from .models import user,postt,comment

# Register your models here.


class stuadmin(admin.ModelAdmin):
    list_display =['name','id','city']

class posttadmin(admin.ModelAdmin):
    list_display =['content','created_by','cr_date']

class commentadmin(admin.ModelAdmin):
    list_display =['postt','user','commented_by','cr_date']

admin.site.register(user,stuadmin)
admin.site.register(postt,posttadmin)
admin.site.register(comment,commentadmin)