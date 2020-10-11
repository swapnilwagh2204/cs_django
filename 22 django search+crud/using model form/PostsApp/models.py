from django.db import models

# Create your models here.


class registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=8)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.username}'


class posts(models.Model):
    author = models.ForeignKey(registration, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
