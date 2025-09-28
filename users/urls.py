from django.urls import path
from .views import SignupView, UserList, UserDetail, CurrentUser

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("", UserList.as_view(), name="user-list"), #amdin-only listing
    path("me/",CurrentUser.as_view(), name="current-user"), #returns logged-in user details
    path("<int:pk>/", UserDetail.as_view(), name="user_detail"),
]