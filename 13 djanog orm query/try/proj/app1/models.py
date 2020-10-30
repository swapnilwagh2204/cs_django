from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    marks = models.FloatField()

    def __str__(self):
        return "Student:-{} \n".format(self.name)


class postt(models.Model):
    content = models.TextField()
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return "Post:-{} \n".format(self.created_by)


