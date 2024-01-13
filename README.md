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
    
    git clone https://github.com/MykleBR/backend-verzel.git
    
    cd inventario-carros-api

Crie um ambiente virtual:

    python -m venv venv

Ative o ambiente virtual:

No Windows:

    .\venv\Scripts\activate

No Unix ou MacOS:

    source venv/bin/activate

Instale as dependências:

    pip install -r requirements.txt



Executando o Servidor de Desenvolvimento

Aplique as migrações:

    python manage.py migrate

Crie um superusuário para acessar o Django admin:

    python manage.py createsuperuser

Inicie o servidor de desenvolvimento:

    python manage.py runserver

Acesse o Django admin em:
    
    http://localhost:8000/admin/
    
faça login usando as credenciais do superusuário.

Documentação da API
Swagger

Explore a API utilizando a documentação Swagger:

    http://localhost:8000/swagger

ReDoc

Alternativamente, visualize a documentação da API com o ReDoc:

    http://localhost:8000/redoc

Estrutura do Projeto

O projeto está organizado da seguinte forma:

    accounts: Autenticação e registro de usuários.
    vehicles: Pontos de extremidade da API para gerenciar o inventário de veículos.
    static/: Arquivos estáticos (CSS, JavaScript, Imagens).
    media/: Arquivos de mídia enviados pelos usuários.
    car_inventory/: Configurações e configurações do projeto.
    manage.py: Script de gerenciamento do Django.
