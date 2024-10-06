from django.conf.urls.static import static
from django.urls import path

from config.settings import dev
from main.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
