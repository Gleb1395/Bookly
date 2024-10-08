from django.urls import path

from accounts.views import (ActiveUserView, DebugPage, UserLoginView,
                            UserLogoutView, UserRegistrationView)

urlpatterns = [
    path("sign-up/", UserRegistrationView.as_view(), name="sign-up"),
    path("sign-in/", UserLoginView.as_view(), name="sign-in"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("activate/<str:uuid>/<str:token>/", ActiveUserView.as_view(), name="activate_user"),
]
