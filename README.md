# express
Projeto de gerenciamento de vendas.

link da aplicação: https://controlexpress.herokuapp.com/

Basta se cadastrar para testar o sistema.

# Executando o projeto localmente

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6.2
3. Ative o virtualenv.
4. Instale as dependências.


# Criando o ambiente virtual

virtualenv sua_env

# Instale os requisitos:

pip install -r requirements.txt

# Crie o banco de dados:

python makemigrations

python manage.py migrate

# Finalmente, execute o servidor de desenvolvimento:

python manage.py runserver

O projeto estará disponível em 127.0.0.1:8000


