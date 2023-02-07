# Entrega 3 Backend

Este projeto consiste em criar uma interface que aceite o upload de um arquivo CNAB, normalize os dados armazene-os em um banco de dados relacional e exiba essa informações em tela.

## Tecnologias Utilizadas:
Python, Django, django restframework.

# Iniciando a aplicação localmente:

1) Clone o repositório usando o ~git clone link_repositório

2) Crie o ambiente virtual com o comando:  python -m venv venv

3) Acesse o ambiente virtual com o comando : source venv/Scripts/activate 

4) Crie o banco de dados usando o comanddo python ~manage.py makemigrations e então rode as migrations com o comando ~python manage.py migrate

5) Instale as dependencias do projeto: pip install -r requirements.txt

6) Cria as tabelas com a sequencia dos comandos: 
python manage.py makemigrations 
python manage.py migrate

1) Execute a aplicação na sua máquina: python manage.py runserver

# End points:

Rota onde deve ser feito o arquivo CNAB:http://127.0.0.1:8000/api/transactions/
Rota para requição dos dados do DB: http://127.0.0.1:8000/api/transactionslist/

