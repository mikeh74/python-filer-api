from filer.models import Image
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from python_filer_api.serializers import FilerImageSerializer


class FilerImageViewSet(ModelViewSet):
    queryset = Image.objects.all().order_by("id")
    serializer_class = FilerImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
