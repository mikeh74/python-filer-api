from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from filer.models import Image
from rest_framework import status
from rest_framework.test import APITestCase


class FilerImageApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="api-user")
        self.image = Image.objects.create(
            original_filename="test.jpg",
            file=self._sample_file(),
            default_alt_text="Existing alt",
            default_caption="Existing caption",
            owner=self.user,
            is_public=True,
        )

    @staticmethod
    def _sample_file():
        return SimpleUploadedFile("test.jpg", b"file-bytes", content_type="image/jpeg")

    def test_list_images_returns_image_objects(self):
        response = self.client.get(reverse("python-filer-api:image-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.image.id)
        self.assertEqual(response.data[0]["default_alt_text"], "Existing alt")

    def test_patch_updates_image_metadata(self):
        self.client.force_authenticate(self.user)
        response = self.client.patch(
            reverse("python-filer-api:image-detail", kwargs={"pk": self.image.pk}),
            {"default_alt_text": "Updated alt", "default_caption": "Updated caption"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.image.refresh_from_db()
        self.assertEqual(self.image.default_alt_text, "Updated alt")
        self.assertEqual(self.image.default_caption, "Updated caption")
