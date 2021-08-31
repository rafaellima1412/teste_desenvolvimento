from django.test import TestCase
from microservico.models import User


class UserModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(name='Hunter')

    def test_user_object(self):
        """Teste para validar se objeto de usuário é criado."""
        self.assertEqual(self.user.name, 'Hunter')


