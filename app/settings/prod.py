from .base import *

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("PGDATABASE"),
        "USER": getenv("PGUSER"),
        "PASSWORD": getenv("PGPASSWORD"),
        "HOST": getenv("PGHOST"),
        "PORT": int(getenv("PGPORT", 5432)),
        "OPTIONS": {
            "sslmode": "require",
        },
        "DISABLE_SERVER_SIDE_CURSORS": True
    }
}
