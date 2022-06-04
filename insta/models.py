
from django.db import models

# Create your models here.
class Image(models.Model):
    '''
    a model for Image posts 
    '''
   
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length = 60, blank = True)
    image_caption = models.CharField(max_length = 60, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
   
class Profile(models.Model):
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    bio = models.TextField(max_length=500, blank=True, default=f'Cool')
