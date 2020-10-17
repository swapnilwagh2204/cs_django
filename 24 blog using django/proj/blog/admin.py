from blog.models import Post, BlogComment, Tag
from django.contrib import admin
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'content', 'timeStamp']


admin.site.register(Post, PostAdmin)


admin.site.register(BlogComment)

admin.site.register(Tag)
