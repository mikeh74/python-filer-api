from filer.models import Image
from rest_framework import serializers


class FilerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "id",
            "name",
            "description",
            "original_filename",
            "is_public",
            "mime_type",
            "default_alt_text",
            "default_caption",
            "uploaded_at",
            "modified_at",
            "file",
        ]
        read_only_fields = ["id", "uploaded_at", "modified_at", "mime_type"]
