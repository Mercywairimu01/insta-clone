
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
    
    def save_image(self):
        ''' 
        method to save an image  instance 
        '''
        self.save()

    def delete_image(self):
        '''
        method to delete an image instance 
        '''
        self.delete()
        
    def total_likes(self):
        return self.likes.count()    

    
   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    bio = models.TextField(max_length=500, blank=True, default=f'Cool')
    
    def save_profile(self):
        '''
        method to save a user's profile 
        '''
        self.save()

    def delete_profile(self):
        '''
        method to delete a user's profile 
        '''
        self.delete()

    def update_bio(self, new_bio):
        ''' 
        method to update a users profile bio 
        '''
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        ''' 
        method to update a user's profile image 
        '''
        user = User.objects.get(id=user_id)
        self.photo = new_image
        self.save()
    

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'Comment by {self.user}'

    def save_comments(self):
        ''' method to save comment instance '''
        self.save()

class Follow(models.Model):
    
    ''' 
    model for user relations following
    '''
    follower = models.ForeignKey('Profile', related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey('Profile', related_name='followers', on_delete=models.CASCADE)
    
    def __str__(self):
        return '{self.follower} follows {self.followed}'
