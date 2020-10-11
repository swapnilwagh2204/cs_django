from django.contrib import admin
from .models import registration, posts
# Register your models here.


class registrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'gender', 'username', 'password']


admin.site.register(registration, registrationAdmin)


class postsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content', 'date']


admin.site.register(posts, postsAdmin)
