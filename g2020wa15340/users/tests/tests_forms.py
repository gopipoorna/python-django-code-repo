from django.test import TestCase
from users.forms import UserRegistrationForm, UserUpdateForm, UpdateProfileForm
from django.contrib.auth.models import User

class TestForms(TestCase):
    
    def testUserRegistrationForm(self):
        form = UserRegistrationForm(data= {
            "username": 'testuser',
            "first_name": 'test',
            "last_name": 'user',
            "email": 'test@gmail.com',
            "password1": 'Blog@123456',
            "password2": 'Blog@123456'
        })
        
        self.assertTrue(form.is_valid())
        
    def testUserUpdateForm(self):
        form = UserUpdateForm(data= {
            "first_name": 'test',
            "last_name": 'user',
            "email": 'test@gmail.com',
        })
        
        self.assertTrue(form.is_valid())
        
    def testUserUpdateProfileForm(self):
        form = UpdateProfileForm(data= {
            "image" : "default.jpg"
        })
        
        self.assertTrue(form.is_valid())