from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    image = models.ImageField(blank=True)
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    
    
class Images(models.Model):
    image = models.ImageField(blank=True, )
    caption = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    
