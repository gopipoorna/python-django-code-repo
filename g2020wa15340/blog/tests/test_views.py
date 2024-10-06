from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import User

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username = "test",
            password = "blog@123"
            )
        self.post1 = Post.objects.create(
            title = "My 1st blog",
            content = "Hello World!",
            author = User.objects.get(id=1)
            )
    
    def testPostListView(self):
        response = self.client.get(reverse("blog-home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
    
    def testPostAboutView(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')
        
    def testPostDetailView(self):
        response = self.client.get(reverse("post-detail", args=[self.post1.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        
    def testUserPostView(self):
        response = self.client.get(reverse("user-post", args=[self.user1.username]))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/user_posts.html')
    
    def testUserPostCreateView(self):
        res= self.client.login(username="test", password="blog@123")
        self.assertTrue(res, "User logging has failed to create a post!")
        response= self.client.post(reverse("post-create"))
        print("Post Create view",response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')
        logout = self.client.logout()
        self.assertIsNone(logout)
        
    def testPostDeleteView(self):
        res= self.client.login(username="test", password="blog@123")
        self.assertTrue(res, "User logging has failed to create a post!")
        response = self.client.post(reverse("post-delete", args=[1]))
        print("post delete view",response)
        self.assertEquals(response.status_code, 302)
        logout = self.client.logout()
        self.assertIsNone(logout)
        
    def testPostUpdateView(self):
        res= self.client.login(username="test", password="blog@123")
        self.assertTrue(res, "User logging has failed to create a post!")
        response = self.client.post(reverse("post-update", args=[1]))
        print("Post Update view",response)
        self.assertEquals(response.status_code, 200)
        logout = self.client.logout()
        self.assertIsNone(logout)
        
    def testUserPostListView(self):
        res= self.client.login(username="test", password="blog@123")
        self.assertTrue(res, "User logging has failed to create a post!")
        response = self.client.get(reverse("post-update", args=[1]))
        print("Post List View",response)
        self.assertEquals(response.status_code, 200)
        logout = self.client.logout()
        self.assertIsNone(logout)
        # self.assertTemplateUsed(response, 'blog/user_posts.html')
        