
from django.contrib import admin
from .models import student, postt

# Register your models here.


class stuadmin(admin.ModelAdmin):
    list_display = ['name', 'rn', 'marks']


class posttadmin(admin.ModelAdmin):
    list_display = ['content', 'created_by', 'cr_date']
    search_fields = ['content', 'created_by']
    list_filter = ['cr_date']


admin.site.register(student, stuadmin)
admin.site.register(postt, posttadmin)
