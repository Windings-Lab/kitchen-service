from .base import *

MIDDLEWARE.insert(2, "debug_toolbar.middleware.DebugToolbarMiddleware")
INSTALLED_APPS.append("debug_toolbar")

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

INTERNAL_IPS = ["127.0.0.1"]
