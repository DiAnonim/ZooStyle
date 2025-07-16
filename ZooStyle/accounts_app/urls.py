from django.urls import path
from . import views

app_name = 'header.html'

urlpatterns = [
    path("register/", views.SignUpView.as_view(), name="register"),
    path("login/", views.SignInView.as_view(), name="login"),
    path("logout/", views.CustomUserLogoutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/edit/", views.CustomUserUpdateView.as_view(), name="profile_edit"),
]