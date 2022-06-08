from django.test import TestCase
from .models import Profile, Post
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    '''
    Profile model
    '''
    def setUp(self):
        self.user = User.objects.create(username='mishM')

    def tearDown(self):
        self.user.delete()

    def test_new_profile(self):
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)

class PostTest(TestCase): 
    '''
    post model tests
    
    '''
    def setUp(self):
        self.test_user = User(username='Mercy', password='new123')
        self.test_user.save()
        

        self.test_post = Post( author=self.test_user)


    def test_instance(self):
        self.assertTrue(isinstance(self.test_Post, Post))

    def test_save(self):
        self.test_post.save_Post()
        self.assertEqual(len(Post.objects.all()),1)

    def tearDown(self):
        self.test_user.delete()
        Post.objects.all().delete()