from django.db import models

# Create your models here.


class Users(models.Model):
    Username = models.CharField(max_length=20, unique=True)
    Password = models.CharField(max_length=10)
    Fullname = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
