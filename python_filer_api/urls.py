from django.urls import include, path
from rest_framework.routers import DefaultRouter

from python_filer_api.views import FilerImageViewSet

app_name = "python-filer-api"

router = DefaultRouter()
router.register("images", FilerImageViewSet, basename="image")

urlpatterns = [
    path("", include(router.urls)),
]
