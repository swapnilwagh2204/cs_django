from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-details',kwargs={'pk':self.id})


    def __str__(self):
        return f'{self.title}'