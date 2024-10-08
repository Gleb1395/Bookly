import uuid

from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, TemplateView

from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.services.send_registration_email import send_registration_email
from accounts.utils.token_generator import TokenGenerator


# def send_test_email(request: HttpRequest) -> HttpResponse:
#     send_mail(
#         subject="Test email",
#         message="Test email, BRO",
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[settings.EMAIL_HOST_USER, "gleb1395@gmail.com"],
#         fail_silently=settings.EMAIL_FAIL_SILENTLY,
#     )
#     return HttpResponse("SUPER!!!")


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
            login(request, current_user)
            return super().get(request, *args, **kwargs)
        return HttpResponse("Wrong data!!!")

class DebugPage(TemplateView):
    template_name = 'emails/registration_email.html'
