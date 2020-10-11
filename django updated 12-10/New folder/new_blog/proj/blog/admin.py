from blog.models import Post, BlogComment,Tag
from django.contrib import admin
# Register your models here.
admin.site.register(Post)

admin.site.register(BlogComment)

admin.site.register(Tag)