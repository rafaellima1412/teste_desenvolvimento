from django.test import TestCase
from microservico.api.serializers import UserSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.user = {
            "name": "hunter",
        }

    def test_success_serializer(self):
        serializer = UserSerializer(data=self.user)
        self.assertTrue(serializer.is_valid())
