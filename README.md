# PI1-SI-2026-Time04 - SCSC
## Sistema de Controle de Solicitações Corporativas

O SCSC é um projeto acadêmico que simula a contratação de uma equipe de desenvolvimento para implementar um sistema interno de uma organização/empresa. A empresa vem enfrentando problemas no gerenciamento de demandas internas, devido a falta de padronização das solicitações. Para isso, o SCSC entra como solução, atuando como um sistema que permite registrar solicitações, classificá-las automaticamente por prioridade e acompanhar seu status.

# Integrantes
- Anita Barbosa
- Ivan Henrique
- Maria Daon
- Miguel Souza

---

# 1. Tecnologias Utilizadas
-   **Linguagem:** Python
- **Banco de Dados** MySQL
- **Versionamento**: Git e GitHub

---

# 2. Interface 
- Aplicação em modo texto (CLI - Terminal)

--- 

# 3. Requisitos Funcionais

## RF01 – Cadastro de Solicitante
Cadastrar e listar solicitantes com validação básica de dados.

| Campo      | Tipo         | Descrição                                                   | Obrigatório |
|------------|--------------|-------------------------------------------------------------|-------------|
| id_usuario | INT          | Identificador numérico gerado automaticamente (PK).        | Sim         |
| nome       | VARCHAR(100) | Nome completo do solicitante.                               | Sim         |
| email      | VARCHAR(100) | E-mail único para identificação (Regra de unicidade).      | Sim*        |
| telefone   | VARCHAR(20)  | Número de telefone para contato.                            | Sim*        |

## RF02 – Abertura de Solicitação
Registrar solicitação vinculada ao solicitante, contendo tipo/categoria, descrição, data/hora e status inicial.

| Campo           | Tipo         | Descrição                                                                 | Obrigatório |
|-----------------|--------------|---------------------------------------------------------------------------|-------------|
| id_solicitacao  | INT          | Identificador único do chamado (PK com Auto Incremento).                 | Sim         |
| id_usuario      | INT          | Chave estrangeira (FK) vinculada a um usuário existente.              | Sim         |
| categoria       | VARCHAR(50)  | Tipo/categoria da solicitação (ex: Hardware, Software).                  | Sim         |
| descricao       | TEXT         | Detalhamento claro do problema (mínimo de caracteres a definir).         | Sim         |
| urgencia        | INT          | Fator numérico para cálculo (Escala de 1 a 3).                         | Sim         |
| impacto         | INT          | Fator numérico para cálculo (Escala de 1 a 3).                          | Sim         |
| prioridade      | VARCHAR(20)  | Resultado do cálculo automático (Baixa, Média, Alta).                 | Sim         |
| status          | VARCHAR(20)  | Status atual (Inicia como 'Aberta').                                    | Sim         |
| data_abertura   | DATETIME     | Registro automático de data e hora no momento da criação.                | Sim         |

# Fluxo de "Acompanhamento e Consultas"

## Fluxo Principal
- O usuário acessa o menu principal.
- O usuário escolhe a opção **"Acompanhamento e Consultas"**.

## Fluxo de Consulta e Listagem
- O usuário escolhe a opção **"Consultar solicitações"**.
- O sistema oferece as opções de filtro:
  - Por Status
  - Por Prioridade
  - Por Usuário
- O sistema executa a query no MySQL com base no filtro escolhido.
- O sistema exibe uma lista organizada contendo:
  - ID Solicitante
  - Categoria
  - Prioridade
  - Status
  - Data
- O sistema retorna ao menu de **"Acompanhamento e Consultas"**.

## Fluxo de Atualização de Status
- O usuário escolhe a opção **"Atualizar Status"**.
- O usuário informa o ID da solicitação que deseja alterar.
- O sistema apresenta a lista de opções:
  - 1 - Aberta
  - 2 - Em andamento
  - 3 - Fechada
- O usuário escolhe uma opção.
- O sistema valida a transição (não permitir alterar solicitações fechadas).
- O novo status é atualizado no banco de dados.
- O sistema exibe a mensagem de confirmação:
  - *Status atualizado com sucesso*.
- O sistema retorna ao menu de **"Acompanhamento e Consultas"**.

## Fluxo de Estatísticas Básicas
- O usuário escolhe a opção **"Ver estatísticas"**.
- O sistema realiza a contagem de registros por status e prioridade.
- O sistema exibe:
  - Total de solicitações por Status
  - Total de solicitações por Prioridade
- O sistema retorna ao menu de **"Acompanhamento e Consultas"**.

## RF03 –  Prioridade Automática
Definir regra objetiva para cálculo automático de prioridade (Baixa/Média/Alta) e armazenar no banco.

## RF04 – Acompanhamento e Consultas
Permitir atualizar status (Aberta/Em andamento/Fechada) e realizar consultas e estatísticas básicas.
