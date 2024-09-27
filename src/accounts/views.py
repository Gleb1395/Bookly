from django.conf import settings


from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse



def send_test_email(request: HttpRequest) -> HttpResponse:
    send_mail(
        subject="Test email",
        message="Test email, BRO",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER, "gleb1395@gmail.com"],
        fail_silently=settings.EMAIL_FAIL_SILENTLY,
    )
    return HttpResponse("SUPER!!!")
