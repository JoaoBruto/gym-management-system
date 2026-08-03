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
- [ ] Atualização de dados
- [ ] Exclusão de alunos
- [ ] Controle de mensalidades (paga / pendente)

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
- [ ] Etapa 5 — Atualizar aluno
- [ ] Etapa 6 — Excluir aluno

## 📚 Aprendizados

Projeto desenvolvido com foco em consolidar:
- Conexão Python ↔ MySQL
- Operações CRUD
- Modelagem de banco de dados
- Uso de Git/GitHub com commits organizados

---

*Projeto em desenvolvimento contínuo!*
