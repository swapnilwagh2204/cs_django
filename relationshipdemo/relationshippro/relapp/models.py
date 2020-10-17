from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.tag_name}'

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    text = models.CharField(max_length=50)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'


class Employee(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


