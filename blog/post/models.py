from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
from django.utils import timezone
from django.urls import reverse
# Create your models here.



class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(null=True,max_length=1000)
    phone = models.CharField(null=True,max_length=11)
    profile_pic = models.ImageField(null=True , blank=True)

    def __str__(self):
        return self.name


class blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=1000)
    title = models.CharField(max_length = 100)
    date=models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog-detail' , kwargs={'pk':self.pk})

    
    
