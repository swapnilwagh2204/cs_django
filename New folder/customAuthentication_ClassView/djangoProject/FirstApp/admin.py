from django.contrib import admin
from .models import Employee
# Register your models here.

class EmloyeeAdmin(admin.ModelAdmin):
    list_display = ['ename', 'ecity','uname','pas']

admin.site.register(Employee, EmloyeeAdmin)