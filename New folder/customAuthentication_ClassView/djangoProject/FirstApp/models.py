from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=20)
    ecity = models.CharField(max_length=10)
    uname = models.CharField(max_length=8)
    pas = models.CharField(max_length=10)