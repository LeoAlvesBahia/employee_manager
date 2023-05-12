# IGS Employee Manager

O "IGS Employee Manager" é um aplicativo web desenvolvido em Django para gerenciar informações de colaboradores, como nome, endereço de e-mail e departamento. Ele possui um painel administrativo, uma API para integrações e um site público para visualização dos detalhes dos colaboradores.

## Requisitos

- Python 3.10
- Django 4.2

## Instalação

1. Clone o repositório:
    ```bash
        git clone https://github.com/seu-usuario/igs-employee-manager.git
    ```
2. Crie e ative um ambiente virtual:
    ```bash
        python3 -m venv venv
        source venv/bin/activate
    ```
3. Instale dependencias:
    ```bash
        pip install -r requirements.txt
    ```
4. Aplique as migrações do banco de dados:
    ```bash
        python manage.py migrate
    ```
5. Execute o servidor de desenvolvimento:
    ```bash
        python manage.py runserver
    ```
6. Acesso o aplicativo em seu navegador pelo endereço `http://localhost:8000`.

## Funcionalidades

Painel Administrativo -> http://localhost:8000/admin: Acesse o painel administrativo do Django para gerenciar os dados dos colaboradores e departamentos. 

API:

    Listar Colaboradores:
        Método: GET
        Endpoint: /api/employees/

    Adicionar Colaborador:
        Método: POST
        Endpoint: /api/employees/
        Corpo da Requisição: JSON contendo os dados do colaborador

    Remover Colaborador:
        Método: DELETE
        Endpoint: /api/employees/{employee_id}/

    Listar Departamentos:
        Método: GET
        Endpoint: /api/departments/

    Adicionar Departamento:
        Método: POST
        Endpoint: /api/departments/
        Corpo da Requisição: JSON contendo os dados do departamento

    Remover Departamento:
        Método: DELETE
        Endpoint: /api/departments/{department_id}/

Website Público -> http://localhost:8000/employees/: Visualize uma tabela simples listando todos os colaboradores e seus respectivos departamentos.

## Licença

Este projeto está licenciado sob a Licença MIT.