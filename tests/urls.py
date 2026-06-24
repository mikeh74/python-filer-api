from django.urls import include, path

urlpatterns = [
    path("api/filer/", include("python_filer_api.urls")),
]
