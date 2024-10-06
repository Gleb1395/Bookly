from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.settings import dev

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("user/", include("accounts.urls")),
]
