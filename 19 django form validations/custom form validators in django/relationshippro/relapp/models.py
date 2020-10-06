from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)


class Comments(models.Model):
    text = models.CharField(max_length=50)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User,on_delete=models.CASCADE)

class Cummunity(models.Model):
    cummunity_name=models.CharField(max_length=20)
    user = models.ManyToManyField(User ,related_name='cummunity')


class EmpReg(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.username}'