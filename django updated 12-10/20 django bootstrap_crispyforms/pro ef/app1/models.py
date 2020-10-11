from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    rn=models.IntegerField()
    marks=models.FloatField()
    subject=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    
    def __str__(self):
       return "name:-{}\n rollno:-{}\n marks:-{}\n subject:-{}".format(self.name, self.rn, self.marks)
