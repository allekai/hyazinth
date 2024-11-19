from django.urls import path

from .views import (
    ProfileUpdateView,
    SignUpView,
    LogoutUserView,
    ProfileView,
    UserListView,
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/update", ProfileUpdateView.as_view(), name="profile_update"),
    path("profile/list", UserListView.as_view(), name="user_list"),
]
