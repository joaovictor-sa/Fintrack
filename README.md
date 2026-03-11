# 🚀 FinTrack — Controle Financeiro Inteligente

![Python Version](https://img.shields.io/badge/python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Django Version](https://img.shields.io/badge/django-5.0-green?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-important?style=for-the-badge)

O **FinTrack** é uma aplicação completa para gestão de finanças pessoais. Ele permite o registro de receitas e despesas, organização por categorias, definição de metas e visualização de dados via Dashboard e API.

A aplicação foi desenhada para ser executada em containers, garantindo que o ambiente de desenvolvimento seja idêntico ao de produção.

---

## ✨ Funcionalidades

* **Gestão de Transações:** CRUD completo de receitas e despesas.
* **Filtros Avançados:** Busca por título, tipo e mês de referência.
* **Categorias e Metas:** Organização de gastos e acompanhamento de objetivos (Goals).
* **Autenticação:** Sistema de login seguro com isolamento de dados por usuário.
* **API REST:** Endpoints integrados via Django REST Framework.
* **Automação:** Migrações e dados iniciais (seed) carregados automaticamente via Docker.

---

## 🛠️ Tecnologias

* **Backend:** Python 3.12 & Django 5.x
* **API:** Django REST Framework
* **Banco de Dados:** PostgreSQL 16 (Alpine)
* **Servidor:** Gunicorn / Django Dev Server
* **Container:** Docker & Docker Compose

---

## 📦 Como rodar o projeto

Graças à automação do Docker, você só precisa de **um passo** para subir a aplicação completa (Banco de Dados + Web Server + Migrações + Dados Iniciais).

### Pré-requisitos
* [Docker](https://www.docker.com/) instalado.
* [Docker Compose](https://docs.docker.com/compose/install/) instalado

### Passo Único

1.  **Clone o projeto e suba os containers:**
    ```bash
    git clone [https://github.com/joaovictor-sa/Fintrack.git](https://github.com/joaovictor-sa/Fintrack.git)
    cd Fintrack
    docker-compose up --build
    ```

**O que acontece agora?**
O Docker irá:
1.  Subir o banco PostgreSQL e aguardar ele estar saudável (`healthcheck`).
2.  Executar as **migrações** (`migrate`) automaticamente.
3.  Popular o banco com dados de teste (`seed_demo_data`).
4.  Disponibilizar o sistema em [http://localhost:8000](http://localhost:8000).

---

## 📁 Estrutura de Pastas

* `/transactions`: Gestão de lançamentos financeiros.
* `/categories`: Organização de categorias.
* `/goals`: Metas de gastos.
* `/fintrack`: Configurações globais do projeto.
* `Dockerfile` & `docker-compose.yml`: Orquestração do ambiente.

---

## 📝 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---
💡 *Desenvolvido por [João Victor](https://github.com/joaovictor-sa)*
