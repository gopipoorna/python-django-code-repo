from django.urls import path
from django.contrib.auth import views
from .views import register, profile

urlpatterns = [
    path('register/', register, name="user-register"),
    path("login/", views.LoginView.as_view(template_name="users/login.html"), name="user-login"),
    path("logout/", views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
    path("password-reset/", views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path("password-reset-done/", views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
    path("profile/", profile, name="user-profile")
]