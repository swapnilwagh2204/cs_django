from django.db import models

# Create your models here.

class Users(models.Model):
    Username = models.CharField(max_length=20,unique=True)
    Password = models.CharField(max_length=50)
    Fullname = models.CharField(max_length=20)
    Address = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.Username}"


class postt(models.Model):
    overview=models.ForeignKey(Users,on_delete=models.CASCADE)
    content=models.TextField()
    created_by=models.CharField(max_length=100)
    cr_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "content:-{} \n created by:-{} \n cr_date:-{} \n".format(self.content, self.created_by, self.cr_date)





