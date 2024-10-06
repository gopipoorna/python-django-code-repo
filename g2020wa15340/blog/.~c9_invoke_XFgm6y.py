from django.test import TestCase
from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView

# Create your tests here.

# Testing URLS

from django.test import SimpleTestCase

class TestUrls(SimpleTestCase):
    
    def testPostCreateView(self):
        assert 1 == 1