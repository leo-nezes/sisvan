<h1 align="center">
  🚧 Documentação em desenvolvimento 🚧
</h1>

<h1 align="center">
  SISVAN
</h1>

### 1. Pré-requisitos
Intalação dos seguntes softwares:

- [PyCharm Community](https://www.jetbrains.com/pt-br/pycharm/download/)
- [Git](https://git-scm.com/downloads)
- [Python 3.8.6](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [DBeaver](https://dbeaver.io/download/)

### 2. Configurando 
#### 2.1 Ambiente de desenvolvimento
Clonar o projeto

`git clone LINK_DO_PROJETO`

Após instalar o Python, abrir o terminal e verificar se a versão é 3.8.6 

`python --version`

Instalar Pipenv

`pip install pipenv`

Abrir o prjeto pelo Pycharm,  e no terminal, criar ambiente virtual

`pipenv --three`

#### 2.2 Base de dados
No postgreSQL, criar uma base de dados chamada **sisvan**

Na aplicação, abrir o arquivo **config/settings.py**, e certifique-se que os parâmetros **USER**, **PASSWORD**, **HOST** e **PORT** estão corretos.

#### 2.3 Aplicação
Ativar ambiente virtual

`pipenv shell`

Baixar dependências do projeto

`pipenv install`

Migrar as tabelas do projeto

`python manage.py migrate`

### 3. Executando aplicação
Executar servidor

`python manage.py runserver`

Acessar aplicação pelo endereço _localhost:8000/sisvan/_ ou _127.0.0.1:8000/sisvan/_
