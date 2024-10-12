from django.urls import path

from accounts.views import (ActiveUserView, UserLoginView, UserLogoutView,
                            UserRegistrationView, ResetPasswordView, PasswordResetConfirmView,
                            PasswordResetCompleteView)

urlpatterns = [
    path("sign-up/", UserRegistrationView.as_view(), name="sign-up"),
    path("sign-in/", UserLoginView.as_view(), name="sign-in"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("activate/<str:uuid>/<str:token>/", ActiveUserView.as_view(), name="activate_user"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
