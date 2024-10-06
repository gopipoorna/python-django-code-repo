from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

class TestModels(TestCase):
    
    def setUp(self):
        
        self.user1 = User.objects.create_user(
            username= "test",
            password= "blog@123"
            )
        
        self.post1 = Post.objects.create(
            title="Demo blog 1",
            content = "This is a demo blog",
            author = self.user1
            )
            
    def testPostModel(self):
        self.assertEqual(self.post1.id, 1)
        self.assertEqual(self.post1.author, self.user1)
        self.assertEqual(self.post1.title, "Demo blog 1")
        self.assertEqual(self.post1.content, "This is a demo blog")
        self.assertEqual(self.post1, Post.objects.get(id=1))
        
        # testing the absolute url path
        self.assertEqual(self.post1.get_absolute_url(), "/post/1/")