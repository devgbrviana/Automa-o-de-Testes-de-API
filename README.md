# 🚀 Automação de Testes de API com Python

Projeto desenvolvido como desafio prático para validação de habilidades em testes automatizados de APIs modernas, utilizando ferramentas atuais do ecossistema Python.

---

## 📌 Objetivo

Estruturar uma base completa de testes automatizados contemplando:

* ✅ Testes de contrato com API externa
* ✅ Testes de performance assíncrona
* ✅ Boas práticas de organização de projeto

---

## 🛠️ Tecnologias Utilizadas

* Python 3.14
* Pytest
* Pytest-Asyncio
* HTTPX
* Tavern
* FastAPI

---

## 📂 Estrutura do Projeto

```
📁 Automa-o-de-Testes-de-API
│
├── api_pagamentos.py          # API simulando processamento assíncrono
├── test_performance.py        # Testes de carga e concorrência
├── test_fluxo_todos.tavern.yaml  # Teste de contrato com API externa
├── utils.py                  # Funções auxiliares de validação
├── .gitignore
└── README.md
```

---

## 🔎 Parte 1: Teste de Contrato (Tavern)

Foi utilizado o Tavern para validar o fluxo da API pública:

👉 https://jsonplaceholder.typicode.com

### ✔️ O que foi implementado:

* Parametrização dos testes (`todo_id`: 1, 5, 15)
* Encadeamento de dados entre requisições (`save`)
* Validação de resposta com função Python (`verify_response_with`)
* Verificação da estrutura da lista retornada

---

## ⚡ Parte 2: Teste de Performance

Teste assíncrono para validar concorrência no endpoint:

```
GET /processar
```

### ✔️ Estratégia:

* Execução de múltiplas requisições simultâneas (5, 20, 50)
* Uso de `asyncio.gather`
* Cliente HTTP assíncrono com `httpx`
* Conexão direta com FastAPI usando `ASGITransport`

### ✔️ Critérios validados:

* Todas requisições retornam status **200**
* Tempo total de execução inferior a **3.5 segundos**

---

## 🧪 Como Executar os Testes

### 1️⃣ Criar e ativar ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 2️⃣ Instalar dependências

```bash
pip install pytest pytest-asyncio httpx tavern fastapi
```

---

### 3️⃣ Executar os testes

```bash
pytest -v
```

---

## 📊 Resultados Esperados

Todos os testes devem passar com sucesso:

```
6 passed
```

---

## 📌 Boas Práticas Aplicadas

* Isolamento de ambiente com `venv`
* Separação de responsabilidades
* Testes declarativos (YAML) + programáticos (Python)
* Execução assíncrona para ganho de performance
* Uso de `.gitignore` para evitar arquivos desnecessários no repositório

---

## 👨‍💻 Autor

Gabriel de Souza Viana

---

## 💡 Considerações Finais

Este projeto demonstra a aplicação prática de testes automatizados em APIs modernas, incluindo:

* Validação de contratos
* Testes de integração
* Testes de performance

Abordagem alinhada com cenários reais de mercado, especialmente em arquiteturas baseadas em microsserviços.
