from django.db import models

# Create your models here.
class employees(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    salary=models.FloatField()
    

