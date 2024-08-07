from django.urls import path
from django.contrib.auth import views
from .views import register, profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', register, name="user-register"),
    path("login/", views.LoginView.as_view(template_name="users/login.html"), name="user-login"),
    path("logout/", views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
    path("profile/", profile, name="user-profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

