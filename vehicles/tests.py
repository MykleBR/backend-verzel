from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class VehiclesViewsTestCase(APITestCase):
    def setUp(self):
        # Cria um usuário administrador para os testes
        self.admin_user = User.objects.create_superuser('vehicles', 'vehicles@example.com', 'vehicles')
        # Cria um veículo de exemplo para os testes
        self.veiculo_data = {'nome': 'Veiculo Teste', 'marca': 'Marca Teste', 'modelo': 'Modelo Teste'}
        self.url_veiculos = reverse('veiculo-list-create')  # Nome da URL para listar/criar veículos
        self.url_login = reverse('login')  # Nome da URL para login

    def get_admin_token(self):
        # Obtém o token JWT para o usuário administrador
        data = {'username': 'vehicles', 'password': 'vehicles'}
        response = self.client.post(self.url_login, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['access']
        return token


    def test_user_login_and_delete(self):
        # Testa o login com as credenciais do usuário criado
        data = {'username': 'vehicles', 'password': 'vehicles'}

        response_login = self.client.post(self.url_login, data)
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)

    def test_veiculo_create_update_delete(self):
        # Obtém o token JWT para o usuário administrador
        token = self.get_admin_token()
        print(token)
        # Adiciona o token JWT ao cabeçalho de autenticação
        headers = {'Authorization': f'Bearer {token}'}

        # Testa a criação de um novo veículo com autenticação do usuário administrador
        response_create = self.client.post(self.url_veiculos, self.veiculo_data, headers=headers)
        print(response_create.data)  # Adicione esta linha para verificar a resposta da criação do veículo
        self.assertEqual(response_create.status_code, status.HTTP_201_CREATED)
        veiculo_id = response_create.data['id']
        self.assertIn('nome', response_create.data)
        self.assertEqual(response_create.data['nome'], self.veiculo_data['nome'])

        # Testa a atualização do veículo criado
        updated_data = {'nome': 'Veiculo Atualizado', 'marca': 'Nova Marca', 'modelo': 'Novo Modelo'}
        url_update = reverse('veiculo-detail', kwargs={'id': veiculo_id})  # Corrigido para usar 'id'
        response_update = self.client.put(url_update, updated_data, headers=headers)
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.data['nome'], updated_data['nome'])

        # Testa a exclusão do veículo
        response_delete = self.client.delete(url_update, headers=headers)
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)

        # Verifica se o veículo foi removido corretamente
        response_get = self.client.get(url_update, headers=headers)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        # Exclui o usuário administrador após os testes
        self.admin_user.delete()
