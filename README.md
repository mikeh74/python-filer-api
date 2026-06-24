# python-filer-api

A REST API layer for django-filer built with Django REST framework.

## Features

- CRUD API endpoints for `filer.models.Image`
- Read image objects with metadata fields including alt text
- Update image metadata (including `default_alt_text`) via `PATCH`/`PUT`

## Installation

```bash
pip install python-filer-api
```

Add app dependencies in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # django-filer requirements
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "easy_thumbnails",
    "mptt",
    "polymorphic",
    "filer",
    # DRF + this package
    "rest_framework",
    "python_filer_api",
]
```

Include URLs:

```python
from django.urls import include, path

urlpatterns = [
    path("api/filer/", include("python_filer_api.urls")),
]
```
