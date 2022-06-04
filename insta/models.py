
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
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
    likes = models.ManyToManyField(User, blank=True)
   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    bio = models.TextField(max_length=500, blank=True, default=f'Cool')

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Follow(models.Model):
    
    ''' 
    model for user relations following
    '''
    follower = models.ForeignKey('Profile', related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey('Profile', related_name='followers', on_delete=models.CASCADE)
    
    def __str__(self):
        return '{self.follower} follows {self.followed}'
