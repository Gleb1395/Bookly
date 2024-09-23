from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-_0#chxkmcfc@!myb)8*je4jbm5_bbs50flw29c-79ir(l*9v=t"

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA: F405
    }
}

STATIC_URL = "static/"
