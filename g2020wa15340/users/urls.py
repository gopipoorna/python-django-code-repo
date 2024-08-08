from django.urls import path
from django.contrib.auth import views
from .views import register, profile


urlpatterns = [
    path('register/', register, name="user-register"),
    path("login/", views.LoginView.as_view(template_name="users/login.html"), name="user-login"),
    path("logout/", views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
    path("profile/", profile, name="user-profile")
]


