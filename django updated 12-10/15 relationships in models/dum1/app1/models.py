from django.db import models

# Create your models here.


class student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    marks=models.FloatField()
    subject=models.CharField(max_length=100)  
    
    def __str__(self):
        return f"{self.name}"


class studentinfo(models.Model):
    student=models.OneToOneField(student,on_delete=models.CASCADE)
    mob=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)



class manufact(models.Model):
    comp_name=models.CharField(max_length=100)
    manuf=models.CharField(max_length=100)
    origin_country=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.comp_name}"


class manufactinfo(models.Model):
    manufact=models.ForeignKey(manufact,on_delete=models.CASCADE)
    carname=models.CharField(max_length=100)
    price=models.FloatField()
    trans=models.CharField(max_length=100)
    eng=models.CharField(max_length=100)


class users(models.Model):
    username=models.CharField(max_length=100)
    exp=models.FloatField()

    def __str__(self):
        return f"{self.username}"


class commnunity(models.Model):
    users=models.ManyToManyField(users)
    community_name=models.CharField(max_length=100)
    popularity=models.IntegerField()



