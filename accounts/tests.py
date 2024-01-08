from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class AccountsViewsTestCase(APITestCase):
    def setUp(self):
        # Cria um usuário para os testes
        self.test_user = User.objects.create_user('accounts', 'accounts@example.com', 'accounts')

    def test_user_login_and_delete(self):
        # Testa o login com as credenciais do usuário criado
        url_login = 'http://127.0.0.1:8000/login/'  # Ajuste conforme sua rota de login
        data = {'username': 'accounts', 'password': 'accounts'}

        response_login = self.client.post(url_login, data)
        self.assertEqual(response_login.status_code, 200)

        # Deleta o usuário diretamente
        self.test_user.delete()

        # Verifica se o usuário foi deletado
        user_exists = User.objects.filter(username='accounts').exists()
        self.assertFalse(user_exists)

