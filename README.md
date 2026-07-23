# Agenda Project 

A complete web system for contact management developed with Python and Django. The project allows users to register, log in, and manage their own contact book, including uploading profile pictures for each saved contact.

## Features

*   **User System:** Registration, Login, Logout, and Profile update with password validation.
*   **Contact Management (CRUD):** Create, read, update, and delete contacts associated with the logged-in user.
*   **Image Upload:** Support for adding a profile picture to contacts.
*   **Search:** Search bar to easily find contacts by name, phone, or email.
*   **Pagination:** Organization of the contact list into multiple pages for fluid navigation.
*   **Categorization:** Classification and organization of contacts by dynamic categories.

## Technologies Used

*   **Back-end:** Python 3, Django
*   **Database:** SQLite (Default Django configuration)
*   **Front-end:** HTML5, CSS3, Django Templates

## How to run the project locally

Follow the steps below to run the project on your machine:

1. **Clone this repository:**
```bash
git clone [https://github.com/YOUR-USERNAME/projeto-agenda.git](https://github.com/YOUR-USERNAME/projeto-agenda.git)
```

2. **Access the project folder:**
```bash
cd projeto-agenda
```

3. **Create and activate the virtual environment:**
```bash
python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On Linux/Mac:
source venv/bin/activate
```

4. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run the database migrations:**
```bash
python manage.py migrate
```

6. **Start the local server:**
```bash
python manage.py runserver
```

7. Access the project in your browser through the link: `http://127.0.0.1:8000/`

<br>
<hr>
<br>


# Projeto Agenda 

Um sistema web completo para gerenciamento de contatos desenvolvido com Python e Django. O projeto permite que usuários se cadastrem, façam login e gerenciem sua própria agenda de contatos, incluindo o upload de fotos de perfil para cada contato salvo.

## Funcionalidades

*   **Sistema de Usuários:** Cadastro, Login, Logout e Atualização de perfil com validação de senhas.
*   **Gestão de Contatos (CRUD):** Criar, ler, atualizar e deletar contatos associados ao usuário logado.
*   **Upload de Imagens:** Suporte para adicionar uma foto de perfil aos contatos.
*   **Busca:** Barra de pesquisa para encontrar contatos facilmente pelo nome, telefone ou e-mail.
*   **Paginação:** Organização da lista de contatos em múltiplas páginas para navegação fluida.
*   **Categorização:** Classificação e organização de contatos por categorias dinâmicas.

## Tecnologias Utilizadas

*   **Back-end:** Python 3, Django
*   **Banco de Dados:** SQLite (Configuração padrão do Django)
*   **Front-end:** HTML5, CSS3, Django Templates

## Como executar o projeto localmente

Siga os passos abaixo para rodar o projeto na sua máquina:

1. **Clone este repositório:**
```bash
git clone [https://github.com/SEU-USUARIO/projeto-agenda.git](https://github.com/SEU-USUARIO/projeto-agenda.git)
```

2. **Acesse a pasta do projeto:**
```bash
cd projeto-agenda
```

3. **Crie e ative o ambiente virtual:**
```bash
python -m venv venv

# No Windows:
.\venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Execute as migrações do banco de dados:**
```bash
python manage.py migrate
```

6. **Inicie o servidor local:**
```bash
python manage.py runserver
```

7. Acesse o projeto no seu navegador através do link: `http://127.0.0.1:8000/`