from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from taggit.managers import TaggableManager


class registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=8)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.username}'


class posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
        return self.title
