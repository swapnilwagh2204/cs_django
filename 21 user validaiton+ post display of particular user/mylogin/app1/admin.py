from django.contrib import admin
from .models import Users,postt

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ['Username','Password','Fullname','Address','Gender']


class posttadmin(admin.ModelAdmin):
    list_display =['content','created_by','cr_date']


admin.site.register(Users, UsersAdmin)
admin.site.register(postt,posttadmin)
