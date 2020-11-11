from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=100)
    rn = models.IntegerField()
    marks = models.FloatField()

    def __str__(self):
        return "name:-{}\n rollno:-{}\n marks:-{}".format(self.name, self.rn, self.marks)


class postt(models.Model):
    content = models.TextField()
    created_by = models.CharField(max_length=100)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "content:-{} \n created by:-{} \n cr_date:-{} \n".format(self.content, self.created_by, self.cr_date)
