from django.db import models
from django.contrib.auth.models import User
from PIL  import Image
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images',null =True)
    name = models.CharField(max_length = 60, blank = True)
    caption = models.CharField(max_length = 60, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes =models.IntegerField( blank = True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='images')
    bio = models.TextField(max_length=500, default=f'Cool')
    
    @classmethod
    def search_by_profile(cls, search_term):
        user = cls.objects.get(user=search_term)
        return user

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, **kwargs):
        super().save( **kwargs)
        img = Image.open(self.image.path)

        if img.height > 250 or img.width > 250:
            output_size = (250, 2500)
            img.thumbnail(output_size)
            img.save(self.image.path)
        