from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView

from accounts.forms import (UserLoginForm, UserRegistrationForm,
                            UserResetPasswordForm)
from accounts.services.send_registration_email import send_registration_email
from accounts.utils.token_generator import TokenGenerator


class UserRegistrationView(CreateView):
    template_name = "sign_up.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")  # ToDo Узнать reverse_lazy

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        send_registration_email(user_instance=self.object, request=self.request)
        return super().form_valid(form)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginView(LoginView):
    template_name = "sign_in.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("index")


class ActiveUserView(RedirectView):
    url = reverse_lazy("index")

    def get(self, request, uuid, token, *args, **kwargs):  # NOQA:F811
        try:
            pk = uuid
            current_user = get_user_model().object.get(pk=pk)
        except (get_user_model().DoesNotExist, ValueError, TypeError):
            return HttpResponse("Wrong data!!!")
        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()
            current_user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, current_user)
            return super().get(request, *args, **kwargs)
        return HttpResponse("Wrong data!!!")


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "emails/password_reset.html"
    form_class = UserResetPasswordForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = get_user_model()
        if user.object.filter(email=email).exists():
            return super().form_valid(form)
        return super().form_invalid(form)


class PasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = "emails/password_reset_confirm.html"


class PasswordResetCompleteView(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = "emails/password_reset_complete.html"
