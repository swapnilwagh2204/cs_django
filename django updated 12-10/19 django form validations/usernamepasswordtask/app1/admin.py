
from django.contrib import admin
from .models import emp

# Register your models here.


class empadmin(admin.ModelAdmin):
    list_display =['username','password']
    

admin.site.register(emp,empadmin)

