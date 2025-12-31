# Sistema de Gerenciamento de Biblioteca

Sistema completo de gerenciamento de biblioteca com banco de dados PostgreSQL e API REST desenvolvida em FastAPI.

---

# 📚 BANCO DE DADOS

## 📦 1. Infraestrutura
- [ ] Criar instância **produção** no Docker  
- [ ] Criar instância **desenvolvimento** no Docker  
- [ ] Configurar volumes separados para cada ambiente  
- [ ] Documentar comandos de criação das instâncias  
- [ ] Criar arquivo `docker-compose.yml` padronizando os ambientes  

---

## 🗂️ 2. Modelagem & Banco de Dados
- [x] Criar schemas (`authentication`, `book`, `customer`, `staff`, `process`)  
- [x] Criar tabelas conforme o modelo lógico  
- [x] Criar relacionamentos (PKs, FKs, constraints)  
- [x] Criar *indexes* úteis  
- [ ] Criar *views* de apoio  
- [x] Criar *sequences* (se necessário)  
- [x] Criar *roles* e *grants* por schema  

---

## 🧪 3. Ambiente de Desenvolvimento
- [x] Criar instância Docker separada para **dev**  
- [x] Popular banco de dev com dados fictícios  
- [x] Criar script de reset (`reset_dev.sh`)  
- [x] Criar `init.sql` com estado inicial versionado  

---

## ⚙️ 4. Lógica de Negócio (Functions, Triggers, Procedures)
### Reservas
- [ ] Criar função para validar disponibilidade do livro  
- [ ] Criar trigger BEFORE INSERT na tabela de reservas  
- [ ] Criar função para atualizar status do livro  
- [ ] Criar trigger AFTER INSERT/UPDATE para manter o catálogo atualizado  

### Usuários
- [ ] Criar função de auditoria  
- [ ] Criar trigger de auditoria  

### Empréstimos
- [ ] Criar trigger para impedir devolução incorreta  
- [ ] Criar função para cálculo de multas  

---

## 🔐 5. Segurança
- [ ] Criar roles `admin`, `app_user`, `readonly`  
- [ ] Dar permissões específicas por schema  
- [ ] Revogar permissões públicas  
- [ ] Criar usuários de aplicação separados por ambiente  

---

## 🛠️ 6. Docker & Deploy
- [ ] Criar `docker-compose.yml` com dois serviços (prod/dev)  
- [ ] Incluir pgAdmin no compose  
- [ ] Documentar variáveis de ambiente  
- [ ] Criar scripts de backup e restore  

---

## 📘 7. Documentação do Banco
- [ ] Documentar modelo lógico  
- [ ] Documentar como subir o ambiente  
- [ ] Documentar execução de migrações  
- [ ] Gerar diagrama ERD automático  

---
---

# 🚀 API REST (FastAPI)

## 📁 Estrutura do Projeto

```
library_api/
├── app/
│   ├── main.py                    # Ponto de entrada da aplicação FastAPI
│   ├── api/
│   │   └── v1/                    # Versionamento da API (v1)
│   │       ├── endpoints/         # Rotas organizadas por domínio
│   │       │   ├── auth.py        # Endpoints de autenticação
│   │       │   ├── books.py       # Endpoints de livros
│   │       │   ├── loans.py       # Endpoints de empréstimos
│   │       │   ├── reservations.py # Endpoints de reservas
│   │       │   ├── customers.py   # Endpoints de clientes
│   │       │   └── staff.py       # Endpoints de funcionários
│   │       └── router.py          # Agregador de rotas
│   ├── core/
│   │   ├── config.py              # Configurações da aplicação (.env)
│   │   ├── security.py            # JWT, hash de senhas, autenticação
│   │   └── dependencies.py        # Dependências injetáveis (DB session, user atual)
│   ├── database/
│   │   └── connection.py          # Pool de conexões PostgreSQL
│   ├── models/                    # Schemas Pydantic (DTOs)
│   │   ├── user.py                # UserCreate, UserResponse, UserLogin
│   │   ├── book.py                # BookCreate, BookResponse, BookUpdate
│   │   ├── loan.py                # LoanCreate, LoanResponse
│   │   └── ...                    # Outros schemas
│   ├── repositories/              # Camada de acesso a dados (queries SQL)
│   │   ├── user_repository.py     # CRUD de usuários
│   │   ├── book_repository.py     # CRUD de livros
│   │   └── ...                    # Outros repositories
│   ├── services/                  # Lógica de negócio
│   │   ├── auth_service.py        # Validações de login, registro
│   │   ├── loan_service.py        # Regras de empréstimo, multas
│   │   └── ...                    # Outras regras de negócio
│   └── utils/
│       ├── exceptions.py          # Exceções personalizadas
│       └── helpers.py             # Funções auxiliares
├── tests/
│   ├── unit/                      # Testes unitários
│   └── integration/               # Testes de integração
├── database/
│   └── scripts/                   # Scripts SQL (já existentes)
├── .env                           # Variáveis de ambiente (não versionar)
├── .env.example                   # Exemplo de variáveis de ambiente
├── .gitignore                     # Arquivos ignorados pelo Git
├── requirements.txt               # Dependências Python
└── README.md                      # Este arquivo
```

---

## 📚 Bibliotecas Utilizadas

| Biblioteca | Versão | Propósito |
|-----------|--------|-----------|
| `fastapi` | 0.109.0 | Framework web moderno e rápido |
| `uvicorn` | 0.27.0 | Servidor ASGI para rodar a aplicação |
| `psycopg2-binary` | 2.9.9 | Driver PostgreSQL para Python |
| `pydantic` | 2.5.3 | Validação de dados e serialização |
| `pydantic-settings` | 2.1.0 | Gerenciamento de configurações |
| `python-jose` | 3.3.0 | Criação e validação de tokens JWT |
| `passlib` | 1.7.4 | Hash de senhas com bcrypt |
| `python-multipart` | 0.0.6 | Suporte para upload de arquivos |
| `pytest` | 7.4.4 | Framework de testes |
| `pytest-asyncio` | 0.23.3 | Suporte para testes assíncronos |
| `httpx` | 0.26.0 | Cliente HTTP para testes de API |
| `python-dotenv` | 1.0.0 | Carregamento de variáveis de ambiente |

---

## 🔧 1. Configuração Inicial do Ambiente
- [x] Criar ambiente virtual Python (`venv`)
- [x] Instalar dependências do `requirements.txt`
- [x] Criar arquivo `.env` com variáveis de ambiente
- [x] Criar arquivo `.env.example` para documentação
- [x] Criar estrutura de pastas do projeto
- [x] Configurar `.gitignore`
- [x] Executar scripts SQL no PostgreSQL
- [x] Ajustar coluna `password` para VARCHAR(255) no banco

---

## 🏗️ 2. Implementação Base
- [x] Criar `app/core/config.py` - Carregar configurações do `.env`
- [x] Criar `app/database/connection.py` - Pool de conexões PostgreSQL
- [x] Criar `app/core/security.py` - Hash de senhas e JWT
- [x] Criar `app/core/dependencies.py` - Injeção de dependências
- [x] Criar `app/main.py` - Inicializar FastAPI
- [x] Testar conexão com banco de dados

---

## 🔐 3. Sistema de Autenticação
- [x] Criar `app/models/user.py` - Schemas de usuário
- [x] Criar `app/repositories/user_repository.py` - CRUD de usuários
- [ ] Criar `app/services/auth_service.py` - Lógica de autenticação
- [ ] Criar endpoint `POST /api/v1/auth/register` - Cadastro
- [ ] Criar endpoint `POST /api/v1/auth/login` - Login (retorna JWT)
- [ ] Criar endpoint `GET /api/v1/auth/me` - Usuário autenticado
- [ ] Implementar middleware de autenticação JWT
- [ ] Testar fluxo completo de autenticação

---

## 📖 4. Módulo de Livros
- [ ] Criar `app/models/book.py` - Schemas de livros
- [ ] Criar `app/repositories/book_repository.py` - CRUD de livros
- [ ] Criar `app/services/book_service.py` - Lógica de negócio
- [ ] Criar endpoint `GET /api/v1/books` - Listar livros (paginação)
- [ ] Criar endpoint `GET /api/v1/books/{id}` - Detalhes do livro
- [ ] Criar endpoint `POST /api/v1/books` - Adicionar livro (admin)
- [ ] Criar endpoint `PUT /api/v1/books/{id}` - Atualizar livro (admin)
- [ ] Criar endpoint `DELETE /api/v1/books/{id}` - Remover livro (admin)
- [ ] Implementar filtros e busca
- [ ] Implementar ordenação de resultados

---

## 📤 5. Módulo de Empréstimos
- [ ] Criar `app/models/loan.py` - Schemas de empréstimos
- [ ] Criar `app/repositories/loan_repository.py` - CRUD de empréstimos
- [ ] Criar `app/services/loan_service.py` - Regras de negócio
- [ ] Criar endpoint `POST /api/v1/loans` - Realizar empréstimo
- [ ] Criar endpoint `GET /api/v1/loans` - Listar todos empréstimos (admin)
- [ ] Criar endpoint `GET /api/v1/loans/my` - Meus empréstimos
- [ ] Criar endpoint `PUT /api/v1/loans/{id}/return` - Devolver livro
- [ ] Implementar validação de disponibilidade do livro
- [ ] Implementar cálculo automático de data de devolução
- [ ] Implementar lógica de multas por atraso

---

## 🔖 6. Módulo de Reservas
- [ ] Criar `app/models/reservation.py` - Schemas de reservas
- [ ] Criar `app/repositories/reservation_repository.py` - CRUD de reservas
- [ ] Criar `app/services/reservation_service.py` - Regras de negócio
- [ ] Criar endpoint `POST /api/v1/reservations` - Fazer reserva
- [ ] Criar endpoint `GET /api/v1/reservations` - Listar todas (admin)
- [ ] Criar endpoint `GET /api/v1/reservations/my` - Minhas reservas
- [ ] Criar endpoint `DELETE /api/v1/reservations/{id}` - Cancelar reserva
- [ ] Implementar validação de limite de reservas por usuário
- [ ] Implementar notificação quando livro ficar disponível

---

## 👥 7. Módulo de Clientes
- [ ] Criar `app/models/customer.py` - Schemas de clientes
- [ ] Criar `app/repositories/customer_repository.py` - CRUD de clientes
- [ ] Criar endpoint `GET /api/v1/customers` - Listar clientes (admin)
- [ ] Criar endpoint `GET /api/v1/customers/{id}` - Detalhes do cliente
- [ ] Criar endpoint `PUT /api/v1/customers/{id}` - Atualizar dados
- [ ] Criar endpoint `GET /api/v1/customers/{id}/history` - Histórico de empréstimos

---

## 👨‍💼 8. Módulo de Funcionários
- [ ] Criar `app/models/staff.py` - Schemas de funcionários
- [ ] Criar `app/repositories/staff_repository.py` - CRUD de funcionários
- [ ] Criar endpoint `GET /api/v1/staff` - Listar funcionários (admin)
- [ ] Criar endpoint `GET /api/v1/staff/{id}` - Detalhes do funcionário
- [ ] Criar endpoint `POST /api/v1/staff` - Adicionar funcionário (admin)
- [ ] Criar endpoint `PUT /api/v1/staff/{id}` - Atualizar funcionário
- [ ] Implementar sistema de permissões por cargo

---

## 💰 9. Módulo de Multas
- [ ] Criar `app/models/fine.py` - Schemas de multas
- [ ] Criar `app/repositories/fine_repository.py` - CRUD de multas
- [ ] Criar endpoint `GET /api/v1/fines/my` - Minhas multas
- [ ] Criar endpoint `GET /api/v1/fines` - Todas multas (admin)
- [ ] Criar endpoint `PUT /api/v1/fines/{id}/pay` - Pagar multa
- [ ] Implementar cálculo automático de multas
- [ ] Implementar bloqueio de empréstimos com multas pendentes

---

## ⚙️ 10. Funcionalidades Avançadas
- [ ] Implementar paginação genérica em todos os endpoints de listagem
- [ ] Implementar sistema de filtros avançados
- [ ] Implementar upload de imagens (capas de livros)
- [ ] Implementar rate limiting
- [ ] Implementar logging estruturado
- [ ] Implementar middleware de tratamento de erros
- [ ] Criar sistema de notificações (email/SMS)
- [ ] Implementar cache com Redis (opcional)

---

## 🧪 11. Testes
- [ ] Configurar ambiente de testes com banco separado
- [ ] Criar fixtures do pytest
- [ ] Testes unitários - `auth_service.py`
- [ ] Testes unitários - `loan_service.py`
- [ ] Testes unitários - `book_service.py`
- [ ] Testes de integração - Endpoints de autenticação
- [ ] Testes de integração - Endpoints de livros
- [ ] Testes de integração - Endpoints de empréstimos
- [ ] Testes de integração - Endpoints de reservas
- [ ] Configurar coverage report
- [ ] Meta: 80%+ de cobertura de código

---

## 📝 12. Documentação da API
- [ ] Adicionar descrições detalhadas em todos os endpoints
- [ ] Adicionar exemplos de request/response
- [ ] Documentar códigos de erro e mensagens
- [ ] Adicionar tags para organizar endpoints no Swagger
- [ ] Criar arquivo `API.md` com guia de uso
- [ ] Documentar fluxos de autenticação
- [ ] Documentar regras de negócio principais

---

## 🚀 13. Deploy e Produção
- [ ] Criar `Dockerfile` para a aplicação
- [ ] Criar `docker-compose.yml` completo (API + PostgreSQL)
- [ ] Configurar variáveis de ambiente para produção
- [ ] Implementar health check endpoint
- [ ] Configurar CORS adequadamente
- [ ] Implementar HTTPS/SSL
- [ ] Documentar processo de deploy
- [ ] Criar scripts de backup automatizados

---

## 🔒 14. Segurança
- [ ] Implementar validação rigorosa de entrada de dados
- [ ] Implementar proteção contra SQL Injection
- [ ] Implementar rate limiting por IP
- [ ] Adicionar headers de segurança (CORS, CSP, etc.)
- [ ] Implementar refresh tokens
- [ ] Adicionar logs de auditoria
- [ ] Implementar bloqueio de conta após tentativas falhas
- [ ] Revisar permissões e roles

---

## 📊 15. Monitoramento
- [ ] Implementar logging estruturado
- [ ] Configurar métricas de performance
- [ ] Criar dashboard de monitoramento
- [ ] Implementar alertas de erro
- [ ] Documentar indicadores-chave (KPIs)

---

## 🎯 Como Usar Este README

1. Marque os itens conforme for completando: `- [x]`
2. Adicione notas ou observações diretamente nos itens, se necessário
3. Mantenha o documento atualizado durante todo o projeto

---

## 🤝 Contribuindo

Este é um projeto educacional. Sinta-se livre para sugerir melhorias!
