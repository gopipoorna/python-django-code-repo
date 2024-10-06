from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username = "test",
            password = "blog@123"
            )
    
    def testRegisterView(self):
        response = self.client.post(reverse("user-register"), 
        {
            "username":"demouser", 
            "first_name":"demo", 
            "last_name":"user", 
            "password1": "somepassword", 
            "password2":"somepassword", 
            "email":"demouser@gmail.com"
            
        })
        user1 = User.objects.get(id=2)
        self.assertEquals(user1.username, "demouser")
        
    def testLoginView(self):
        response = self.client.post(reverse("user-login"), {"username": "test", "password":"blog@123"})
        print(response)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.client.session.get('_auth_user_id'), str(self.user1.id))
        
    def testLogoutView(self):
        response = self.client.get(reverse("user-logout"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/logout.html")
        self.assertEquals(self.client.session.get('_auth_user_id'), None)
        self.assertNotEquals(self.client.session.get('_auth_user_id'), str(self.user1.id))
        
    def testPasswordResetView(self):
        response = self.client.get(reverse("password_reset"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset.html")
        
    def testPasswordResetDoneView(self):
        response = self.client.get(reverse("password_reset_done"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset_done.html")
        
    def testPasswordResetConfirmView(self):
        response = self.client.get(reverse("password_reset_confirm", args=['aidb', 'fdfsfsd']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset_confirm.html")
        
    def testPasswordResetCompleteView(self):
        response = self.client.get(reverse("password_reset_complete"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset_complete.html")
        
    def testProfileView(self):
        res= self.client.login(username="test", password="blog@123")
        self.assertTrue(res, "User logging has failed to check the user profile")
        response = self.client.get(reverse("user-profile"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile.html")
        logout = self.client.logout()
        self.assertIsNone(logout)