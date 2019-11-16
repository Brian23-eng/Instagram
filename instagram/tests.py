from django.test import TestCase
from .models import Profiles, Images, Comments
from django.contrib.auth.models import User
import datetime as dt



class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'pip', email='g@gmail.com', password='pip2')
        self.user.save()
        
        self.profile = Profiles(image= '/posts', bio='TGOD', user=self.user)
        self.profile.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profiles))
        
        
    def test_save_method(self):
        # self.bio.save_bio()
        profile =Profiles.objects.all()
        self.assertTrue(len(profile) > 0)
        
    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profiles.objects.all()
        self.assertTrue(len(profile) == 0)
        
    def tearDown(self):
        Images.objects.all().delete()
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.user= User(username='pip',email='go@gmail.com', password='pip2')
        self.user.save()

        self.profile=Profiles(image='/posts',bio='TGOD',user=self.user)
        self.profile.save()
        
        self.image = Images(image='posts/',caption='testing1',pub_date='16/11/2019',profile=self.user,posted=auto_now())
        self.image.save_image()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Images))

    def test_save_image(self):
        self.image.save_image()
        images= Images.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_caption(self):
        self.image.save_image()
        kwargs={'image':'/posts','caption':'dont stop me now'}
        Image.update_caption(self.image.id,**kwargs)
        self.assertEqual("dont stop me now",self.image.caption)


    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Images.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_id(self):
        image_id = id
        self.image.objects.get(pk=id)
        self.assertTrue(pk=id)

    def tearDown(self):
        Images.objects.all().delete()
        
        


