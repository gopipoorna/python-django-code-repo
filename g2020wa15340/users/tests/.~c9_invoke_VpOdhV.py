from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

class TestModels(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create_user(
            username= "test",
            password= "blog@123"
            )
            
    def testProfileModel(self):
        self.assertEquals(self.user1.username)