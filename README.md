# FinTrack

![Python Version](https://img.shields.io/badge/python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Django Version](https://img.shields.io/badge/django-5.0-green?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-important?style=for-the-badge)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange?style=for-the-badge)

# 🚀 FinTrack — Controle Financeiro Inteligente

O **FinTrack** é uma aplicação web completa para gestão de finanças pessoais. O sistema permite o registro de receitas e despesas, organização por categorias, definição de metas de gastos e visualização de dashboards integrados. Desenvolvido com uma arquitetura moderna, o projeto separa a lógica de interface (Django Templates) de uma API robusta (Django REST Framework).

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** [Django 5.x](https://www.djangoproject.com/) & [Python 3.12](https://www.python.org/)
* **API:** [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
* **Banco de Dados:** [PostgreSQL](https://www.postgresql.org/) (via Docker)
* **Containerização:** [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
* **Frontend:** HTML5, CSS3 (Custom styles) & [Bootstrap 5](https://getbootstrap.com/)
* **Ícones:** [Bootstrap Icons](https://icons.getbootstrap.com/)

---

## ✨ Funcionalidades Principais

* **Gestão de Transações:** Cadastro, edição, exclusão e visualização de receitas e despesas.
* **Filtros Inteligentes:** Busca por título, tipo (Entrada/Saída) e mês de referência.
* **Categorização:** Organização de gastos por categorias personalizadas.
* **Metas de Gastos (Goals):** Acompanhamento de objetivos financeiros.
* **Autenticação Segura:** Sistema de login/logout com permissões baseadas em usuário (um usuário não vê os dados do outro).
* **API Integrada:** Endpoints prontos para consumo por outras aplicações ou mobile.

---

## 📦 Como rodar o projeto

### Pré-requisitos
* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/joaovictor-sa/Fintrack.git](https://github.com/joaovictor-sa/Fintrack.git)
    cd Fintrack
    ```

2.  **Suba os containers:**
    O Docker vai configurar automaticamente o Python, o Banco de Dados e as dependências.
    ```bash
    docker-compose up --build
    ```

3.  **Execute as migrações (na primeira vez):**
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4.  **Crie um superusuário (opcional para acessar o /admin):**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5.  **Acesse a aplicação:**
    Abra o navegador em [http://localhost:8000](http://localhost:8000)

---

## 📁 Estrutura do Projeto

* `/transactions`: App principal de gestão de lançamentos financeiros.
* `/categories`: Gestão de categorias de gastos.
* `/goals`: Planejamento e metas financeiras.
* `/fintrack`: Configurações centrais do Django (Settings, URLs).
* `/templates`: Arquivos HTML base e específicos das views.

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
💡 *Desenvolvido por [João Victor](https://github.com/joaovictor-sa)*
