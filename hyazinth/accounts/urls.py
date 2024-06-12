from django.urls import path

from .views import SignUpView, LogoutUserView, ProfileView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]