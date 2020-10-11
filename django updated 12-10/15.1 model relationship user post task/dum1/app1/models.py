from django.db import models

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    city=models.CharField(max_length=100)  
    
    def __str__(self):
        return f"name:-{self.name}"

class postt(models.Model):
    overview=models.ForeignKey(user,on_delete=models.CASCADE)
   
    content=models.TextField()
    created_by=models.CharField(max_length=100)
    cr_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"content:-{self.overview}"


class comment(models.Model):
    postt=models.ForeignKey(postt,on_delete=models.CASCADE)
    user=models.ForeignKey(user,on_delete=models.CASCADE)

    commented_by=models.CharField(max_length=100)
    cr_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"commented_by:-{self.commented_by}"
