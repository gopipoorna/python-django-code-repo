from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView, about, UserPostListView

# Create your tests here.

# Testing URLS

class TestUrls(TestCase):
    
    print("Testing URLs")
    
    def testPostListView(self):
        url = reverse("blog-home")
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostListView)
        
    def testPostDetailView(self):
        url = reverse("post-detail", args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
        
    def testPostCreateView(self):
        url = reverse("post-create")
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostCreateView)
        
    def testPostUpdateView(self):
        url = reverse("post-update", args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)
        
    def testPostDeleteView(self):
        url = reverse("post-delete", args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)
        
    def testAboutView(self):
        url = reverse("blog-about")
        self.assertEquals(resolve(url).func, about)
        
    def testUserPostListView(self):
        url = reverse("user-post", args=['someuser'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView)
        