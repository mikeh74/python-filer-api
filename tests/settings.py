import tempfile


SECRET_KEY = "test-secret-key"
DEBUG = True
SITE_ID = 1

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "easy_thumbnails",
    "mptt",
    "polymorphic",
    "filer",
    "rest_framework",
    "python_filer_api",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ROOT_URLCONF = "tests.urls"
MIDDLEWARE = []
USE_TZ = True
MEDIA_ROOT = tempfile.mkdtemp(prefix="python-filer-api-tests-")
