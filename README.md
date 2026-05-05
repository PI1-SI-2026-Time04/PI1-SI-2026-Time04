# PI1-SI-2026-Time04
## Sistema de Controle de Solicitações Corporativas (SCSC)

O SCSC é um projeto acadêmico que simula a contratação de uma equipe de desenvolvimento para implementar um sistema interno de uma organização/empresa. A empresa vem enfrentando problemas no gerenciamento de demandas internas, devido a falta de padronização das solicitações. Para isso, o SCSC entra como solução, atuando como um sistema que permite registrar solicitações, classificá-las automaticamente por prioridade e acompanhar seu status.

# Integrantes
- Anita Barbosa
- Ivan Henrique
- Maria Daon
- Miguel Souza

---

# 1. Tecnologias Utilizadas
- **IDE:** PyCharm e VS Code
- **Linguagem:** Python
- **Banco de Dados** MySQL
- **Versionamento**: Git e GitHub

---

# 2. Interface 
- Aplicação em modo texto (CLI - Terminal)

---

# 3. Requisitos Funcionais

## RF01 – Cadastro de Solicitante
Cadastrar e listar solicitantes com validação básica de dados.

## RF02 – Abertura de Solicitação
Registrar solicitação vinculada ao solicitante, contendo tipo/categoria, descrição, data/hora e status inicial.

## RF03 –  Prioridade Automática
A prioridade é calculada somando os valores de urgência e impacto.
Fórmula: Prioridade = Urgência + Impacto
| Resultado | Classificação |
|----------|--------------|
| 2 e 3   | Baixa        |
| 4 e 5   | Média        |
| 6        | Alta         |

## RF04 – Acompanhamento e Consultas
Permitir atualizar status (Aberta/Em andamento/Fechada) e realizar consultas e estatísticas básicas.

---

# 4. Estrutura de Dados

O banco de dados utilizado é o **MySQL**, composto por três tabelas principais:

- `solicitantes`
- `solicitacoes`
- `log_prioridade`

---

## Tabela: solicitantes

Armazena os dados dos solicitantes.

| Campo       | Tipo         | Restrições          |
|------------|-------------|---------------------|
| id_usuario | INT         | PK, AUTO_INCREMENT  |
| nome       | VARCHAR(100)| NOT NULL            |
| email      | VARCHAR(100)| NOT NULL, UNIQUE    |
| celular    | VARCHAR(20) | NOT NULL            |

---

## Tabela: solicitacoes

Armazena as solicitações registradas.

| Campo           | Tipo         | Restrições                 |
|-----------------|-------------|----------------------------|
| id_solicitacao  | INT         | PK, AUTO_INCREMENT         |
| id_usuario      | INT         | FK                         |
| categoria       | VARCHAR(50) | NOT NULL                   |
| descricao       | TEXT        | NOT NULL                   |
| urgencia        | INT         | CHECK (1 a 3)              |
| impacto         | INT         | CHECK (1 a 3)              |
| prioridade      | VARCHAR(20) | NOT NULL                   |
| status          | VARCHAR(20) | DEFAULT 'Aberta'           |
| data_abertura   | DATETIME    | DEFAULT CURRENT_TIMESTAMP  |

**Relacionamento:**
- `id_usuario` referencia `solicitantes(id_usuario)`
- Exclusão em cascata (`ON DELETE CASCADE`)

---

## Tabela: log_prioridade

Registra o histórico do cálculo de prioridade.

| Campo           | Tipo         | Restrições                 |
|-----------------|-------------|----------------------------|
| id_log          | INT         | PK, AUTO_INCREMENT         |
| id_solicitacao  | INT         | FK                         |
| urgencia        | INT         | NOT NULL                   |
| impacto         | INT         | NOT NULL                   |
| resultado       | INT         | NOT NULL                   |
| classificacao   | VARCHAR(20) | NOT NULL                   |
| data_registro   | DATETIME    | DEFAULT CURRENT_TIMESTAMP  |

**Relacionamento:**
- `id_solicitacao` referencia `solicitacoes(id_solicitacao)`
- Exclusão em cascata (`ON DELETE CASCADE`)
