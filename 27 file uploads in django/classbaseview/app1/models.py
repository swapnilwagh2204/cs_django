from django.db import models


class Student(models.Model):


    rollno = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.IntegerField()

    def __str__(self):
        return f'rollno:{self.rollno} name:{self.name}'


class Employee(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    name=models.CharField(max_length=20)
    last_login=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f'name:{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=30)
    cover = models.ImageField(upload_to='images')