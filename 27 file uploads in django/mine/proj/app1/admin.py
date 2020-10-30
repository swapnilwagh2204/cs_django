from .models import File
from django.contrib import admin

# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'filepath']


admin.site.register(File, FileAdmin)
