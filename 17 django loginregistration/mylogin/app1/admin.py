from django.contrib import admin
from .models import Users

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ['Username','Password','Fullname','Email','Address','Gender']

admin.site.register(Users, UsersAdmin)
