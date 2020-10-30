from django.contrib import admin
from .models import student, postt
# Register your models here.


class studentadmin(admin.ModelAdmin):
    list_display = ['name', 'rollno', 'marks']


admin.site.register(student, studentadmin)


class posttadmin(admin.ModelAdmin):
    list_display = ['content', 'created_by']


admin.site.register(postt, posttadmin)
