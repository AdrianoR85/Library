# ✔️ Plano do Projeto — Sistema de Reserva de Livros (PostgreSQL + Docker)

## 📦 1. Infraestrutura
- [ ] Criar instância **produção** no Docker  
- [ ] Criar instância **desenvolvimento** no Docker  
- [ ] Configurar volumes separados para cada ambiente  
- [ ] Documentar comandos de criação das instâncias  
- [ ] Criar arquivo `docker-compose.yml` padronizando os ambientes  

---

## 🗂️ 2. Modelagem & Banco de Dados
- [x] Criar schemas (`auth`, `library`, `operation`)  
- [x] Criar tabelas conforme o modelo lógico  
- [x] Criar relacionamentos (PKs, FKs, constraints)  
- [ ] Criar *indexes* úteis  
- [ ] Criar *views* de apoio  
- [ ] Criar *sequences* (se necessário)  
- [ ] Criar *roles* e *grants* por schema  

---

## 🧪 3. Ambiente de Desenvolvimento
- [ ] Criar instância Docker separada para **dev**  
- [ ] Popular banco de dev com dados fictícios  
- [ ] Criar script de reset (`reset_dev.sh`)  
- [ ] Criar `init.sql` com estado inicial versionado  

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

### Empréstimos (se houver)
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

## 📘 7. Documentação
- [ ] Documentar modelo lógico  
- [ ] Documentar como subir o ambiente  
- [ ] Documentar execução de migrações  
- [ ] Gerar diagrama ERD automático  
