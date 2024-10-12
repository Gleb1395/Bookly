from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpRequest
from django.template.loader import render_to_string

from accounts.utils.token_generator import TokenGenerator


def send_registration_email(user_instance: get_user_model(), request: HttpRequest) -> None:
    message = render_to_string(
        template_name="emails/registration_email.html",
        context={
            "user": user_instance,
            "domain": get_current_site(request),
            "token": TokenGenerator().make_token(user_instance),
            "uid": user_instance.pk,
        },
    )
    email = EmailMessage(
        subject=settings.REGISTRATION_EMAIL_SUBJECT,
        body=message,
        to=[user_instance.email],
        cc=None,
    )
    email.content_subtype = "html"
    email.send(fail_silently=settings.EMAIL_FAIL_SILENTLY)
