from django.test import TestCase
from django.urls import reverse, resolve
from users.views import register, profile
from django.contrib.auth import views

# Create your tests here.

class TestUserUrls(TestCase):
    
    def testRegister(self):
        url = reverse("user-register")
        self.assertEquals(resolve(url).func, register)
        
    def testProfile(self):
        url = reverse("user-profile")
        self.assertEquals(resolve(url).func, profile)
        
    def testLogin(self):
        url = reverse("user-login")
        self.assertEquals(resolve(url).func.view_class, views.LoginView)
        
    def testLogout(self):
        url = reverse("user-logout")
        self.assertEquals(resolve(url).func.view_class, views.LogoutView)
        
    def testPasswordReset(self):
        url = reverse("password_reset")
        self.assertEquals(resolve(url).func.view_class, views.PasswordResetView)
        
    def testPasswordResetDone(self):
        url = reverse("password_reset_done")
        self.assertEquals(resolve(url).func.view_class, views.PasswordResetDoneView)
        
    def testPasswordResetConfirm(self):
        url = reverse("password_reset_confirm", args=["uidb64", "somevalue"])
        self.assertEquals(resolve(url).func.view_class, views.PasswordResetConfirmView)
        
    def testPasswordResetComplete(self):
        url = reverse("password_reset_complete")
        self.assertEquals(resolve(url).func.view_class, views.PasswordResetCompleteView)