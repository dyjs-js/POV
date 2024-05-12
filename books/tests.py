from rest_framework.test import APITestCase
from users.models import User
from gptCreate.models import GptPhoto
from .serializers import GptPhotoSerializer

# Create your tests here.


class TestBooks(APITestCase):

    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()

    def test_create_book(self):
        response = self.client.post("/api/v1/books/")
        self.assertEqual(response.status_code, 403)

        self.client.login(
            username="test",
            password="123",
        )
        response = self.client.post("/api/v1/books/")
        print(response.json())


class GptPhotoSerializerTest(APITestCase):

    def setUp(self):
        # 테스트 데이터 생성
        self.gpt_photo = GptPhoto.objects.create(file="example.jpg")
        self.serializer = GptPhotoSerializer(instance=self.gpt_photo)

    def test_gpt_photo_serializer_output(self):
        print(self.serializer.data)
