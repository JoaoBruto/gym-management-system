# 🏋️ Gym Management System

Sistema de gerenciamento de academia desenvolvido em **Python** com **MySQL**, criado como projeto de estudo com foco em CRUD, modelagem de banco de dados e boas práticas de versionamento.

O sistema é pensado como se fosse ser usado por uma academia real: cadastro de alunos, controle de mensalidades e acompanhamento de objetivos (emagrecimento, hipertrofia, etc).

## 🛠️ Tecnologias

- Python 3
- MySQL
- (biblioteca de conexão, ex: `mysql-connector-python`)

## 📋 Funcionalidades

- [x] Cadastro de alunos
- [x] Listagem de alunos
- [x] Busca de alunos
- [x] Atualização de dados
- [x] Exclusão de alunos
- [x] Controle de mensalidades (paga / pendente)
- [x] Menu de interação

## 🗃️ Estrutura do banco de dados

**Tabela `alunos`**

| Campo             | Tipo         | Descrição                              |
|-------------------|--------------|-----------------------------------------|
| id                | INT (PK, AI) | Identificador único                     |
| nome              | VARCHAR(100) | Nome do aluno                           |
| idade             | INT          | Idade do aluno                          |
| telefone          | VARCHAR(20)  | Contato                                 |
| peso              | FLOAT        | Peso (kg)                               |
| altura            | FLOAT        | Altura (m)                              |
| objetivo          | VARCHAR(50)  | Emagrecimento, hipertrofia, etc.        |
| data_matricula    | DATE         | Data de entrada na academia             |
| mensalidade_paga  | BOOLEAN      | Situação da mensalidade                 |


## 🧭 Roadmap do desenvolvimento

- [x] Etapa 0 — Estrutura inicial do projeto
- [x] Etapa 1 — Criar banco e tabela `alunos`
- [x] Etapa 2 — Cadastrar aluno
- [x] Etapa 3 — Listar alunos
- [x] Etapa 4 — Buscar aluno
- [x] Etapa 5 — Atualizar aluno
- [x] Etapa 6 — Excluir aluno

## 📚 Aprendizados

Projeto desenvolvido com foco em consolidar:
- Conexão Python ↔ MySQL
- Operações CRUD
- Modelagem de banco de dados
- Uso de Git/GitHub com commits organizados

## 🚀 Melhorias futuras (V2)

### Segurança e configuração
- [ ] Mover credenciais do banco para variável de ambiente (`python-dotenv`)

### Organização de código
- [ ] Centralizar listas de opções (objetivo, mensalidade) em um único lugar
- [ ] Extrair validações repetidas (idade, peso, altura, telefone) em funções reutilizáveis
- [ ] Separar o projeto em múltiplos arquivos/módulos (conexão, CRUD, menu)

### Robustez
- [ ] Tratar erro de conexão com o banco (try/except ao redor do connect)
- [ ] Adicionar constraint UNIQUE para telefone
- [ ] Pedir confirmação antes de atualizar um dado (não só ao excluir)

### Experiência de uso (UX)
- [ ] Limpar terminal entre ações do menu
- [ ] Formatar listagem como tabela (biblioteca `tabulate`)
- [ ] Mensagens de boas-vindas e despedida no menu

### Novas funcionalidades
- [ ] Busca de aluno por nome parcial (`LIKE`)
- [ ] Contagem total de alunos cadastrados
- [ ] Exportar lista de alunos para `.csv`

### Qualidade
- [ ] Testes automatizados com `pytest`

### Evolução com novas tecnologias (conforme progresso nos estudos)
- [ ] **Git/GitHub avançado:** reorganizar histórico com branches e Issues
- [ ] **Linux:** script de shell para automatizar setup do banco
- [ ] **Redis:** cache para buscas frequentes (ex: listagem)
- [ ] **Node.js:** recriar a camada de dados como API REST
- [ ] **Prisma:** substituir SQL puro por ORM (na versão Node)
- [ ] **Java:** reimplementar o sistema como comparação de stacks
---

*Projeto concluido!*
