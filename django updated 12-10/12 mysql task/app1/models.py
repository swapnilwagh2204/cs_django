from django.db import models

# Create your models here.
class employees(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    salary=models.FloatField()

class student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    marks=models.FloatField()
    subject=models.CharField(max_length=100)

class faculty(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    specialisation=models.CharField(max_length=100)
    salary=models.FloatField()
    just=models.FloatField(default=1000)

    

