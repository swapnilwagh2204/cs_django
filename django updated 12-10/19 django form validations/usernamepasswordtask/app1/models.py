from django.db import models

# Create your models here.


class emp(models.Model):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    
    def __str__(self):
       return f"username:-{self.username}"



