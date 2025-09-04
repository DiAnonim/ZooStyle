from django.urls import path
from accounts_app.views import CustomUserSignUpView, CustomUserLoginView, CustomUserLogoutView, CustomUserProfileView, CustomUserEditView, CustomUserDeleteView

app_name = 'accounts_app'

urlpatterns = [
    path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path("login/", CustomUserLoginView.as_view(), name="login"),
    path("logout/", CustomUserLogoutView.as_view(), name="logout"),
    
    path("profile/", CustomUserProfileView.as_view(), name="profile"),
    path("profile_edit/", CustomUserEditView.as_view(), name="profile_edit"),
    path("profile_delete/", CustomUserDeleteView.as_view(), name="profile_delete"),
]