from django.test import TestCase
from .models import Profiles, Images, Comments
from django.contrib.auth.models import User
import datetime as dt



class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'pip', email='g@gmail.com', password='pip2')
        self.user.save()
        
        self.profile = Profile(image= '/posts', bio='TGOD', user= 'self.user')
        self.profile.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profiles))
        
        
    def test_save_method(self):
        self.bio.save_bio()
        profile =Profiles.objects.all()
        self.assertTrue(len(profile) > 0)
        
    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profiles.objects.all()
        self.assertTrue(len(profile) == 0)
        
    def tearDown(self):
        Images.objects.all().delete()


