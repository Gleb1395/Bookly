from config.settings.base import *  # NOQA

SECRET_KEY = os.getenv("SECRET_KEY")  # NOQA: F405

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA: F405
    }
}

STATIC_URL = "static/"
MEDIA_ROOT = "media/"
MEDIA_URL = "media/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # NOQA F405
]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # NOQA F405
