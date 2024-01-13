API de Inventário de Carros

Bem-vindo à API de Inventário de Carros! Este projeto é construído com o Django REST Framework, conectando-se a um frontend Flutter e implementando autenticação JWT para garantir o acesso seguro do usuário.
Guia Rápido
Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

    Python (versão 3.11.3)
    Pip
    MySQL (Workbench 8.0.33 de preferência)

Instalação

    Clone o repositório:

    bash

git clone https://github.com/MykleBR/backend-verzel.git
cd inventario-carros-api

Crie um ambiente virtual:

bash

python -m venv venv

Ative o ambiente virtual:

    No Windows:

    bash

.\venv\Scripts\activate

No Unix ou MacOS:

bash

    source venv/bin/activate

Instale as dependências:

bash

    pip install -r requirements.txt

Executando o Servidor de Desenvolvimento

    Aplique as migrações:

    bash

python manage.py migrate

Crie um superusuário para acessar o Django admin:

bash

python manage.py createsuperuser

Inicie o servidor de desenvolvimento:

bash

    python manage.py runserver

    Acesse o Django admin em http://localhost:8000/admin/ e faça login usando as credenciais do superusuário.

Documentação da API
Swagger

Explore a API utilizando a documentação Swagger:

    URL: Documentação Swagger

ReDoc

Alternativamente, visualize a documentação da API com o ReDoc:

    URL: Documentação ReDoc

Estrutura do Projeto

O projeto está organizado da seguinte forma:

    accounts: Autenticação e registro de usuários.
    vehicles: Pontos de extremidade da API para gerenciar o inventário de veículos.
    static/: Arquivos estáticos (CSS, JavaScript, Imagens).
    media/: Arquivos de mídia enviados pelos usuários.
    car_inventory/: Configurações e configurações do projeto.
    manage.py: Script de gerenciamento do Django.