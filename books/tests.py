from rest_framework.test import APITestCase
from users.models import User

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
