from .base import *

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


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

STATIC_ROOT = "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media file storage

INSTALLED_APPS += ["storages"]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get("B2_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("B2_APP_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("B2_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.environ.get("B2_ENDPOINT_URL")
AWS_QUERYSTRING_AUTH = True

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_ENDPOINT_URL}/"
