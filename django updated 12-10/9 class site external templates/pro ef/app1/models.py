from django.db import models

# Create your models here.

class User(models.Model):
    subject = models.CharField(max_length=100)
    msg=models.TextField()
    cr_date= models.DateTimeField(auto_now_add=True)
    
