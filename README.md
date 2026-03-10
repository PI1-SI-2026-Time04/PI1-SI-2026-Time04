# PI1-SI-2026-Time04
Projetinho de Python

# Integrantes
- Victor Ramos
- Anita Barbosa
- Maria Daon
- Miguel Souza

# Tecnologias Utilizadas
- Python
- MySQL
- GitHub

# Interface 
- Aplicação em modo texto (CLI - Terminal)

# Requisitos

## RF01 – Cadastro de Solicitante
Cadastrar e listar solicitantes com validação básica de dados.

| Campo               | Descrição                              | Obrigatório |
|--------------------|------------------------------------------|-------------|
| ID do Usuário      | Identificador único do usuário           | Sim         |
| Usuário            | Nome de usuário para acesso ao sistema   | Sim         |
| Senha              | Senha de autenticação do usuário         | Sim         |
| Email              | Email válido do solicitante              | Sim         |
| Departamento       | Departamento ao qual o usuário pertence  | Sim         |
| Telefone           | Número de telefone para contato          | Não         |
| Data de Nascimento | Data de nascimento do solicitante        | Não         |
  
## RF02 – Abertura de Solicitação
Registrar solicitação vinculada ao solicitante, contendo tipo/categoria, descrição, data/hora e status inicial.

| Campo             | Descrição                                                           | Obrigatório |
| ----------------- | ------------------------------------------------------------------- | ----------- |
| ID da Solicitação | Identificador único da solicitação                                  | Sim         |
| Título            | Título resumido da solicitação                                      | Sim         |
| Descrição         | Descrição detalhada do problema ou solicitação                      | Sim         |
| Data de Abertura  | Data e hora em que a solicitação foi registrada                     | Sim         |
| Status            | Situação atual da solicitação (ex: Aberto, Em andamento, Concluído) | Sim         |
| ID do Solicitante | Identificação do solicitante que abriu a solicitação                | Sim         |
| ID da Prioridade  | Prioridade atribuída à solicitação                                  | Sim         |
| ID da Categoria   | Categoria do tipo de solicitação                                    | Sim         |


## RF03 – Prioridade Automática
Definir regra objetiva para cálculo automático de prioridade (Baixa/Média/Alta) e armazenar no banco.

### Tabela Prioridade
| Campo            | Descrição                                                | Obrigatório |
| ---------------- | -------------------------------------------------------- | ----------- |
| ID da Prioridade | Identificador único da prioridade                        | Sim         |
| Nome             | Nome da prioridade (Baixa, Média, Alta, Crítica)         | Sim         |
| Valor            | Valor de 0 a 5 para calcular o peso                      | Sim         |

### Tabela Categoria
| Campo           | Descrição                                                         | Obrigatório |
| --------------- | ----------------------------------------------------------------- | ----------- |
| ID da Categoria | Identificador único da categoria                                  | Sim         |
| Nome            | Nome da categoria da solicitação (Hardware, Software, Rede, etc.) | Sim         |
| Valor           | Valor de 0 a 5 para calcular o peso                               | Sim         |

## RF04 – Acompanhamento e Consultas
Permitir atualizar status (Aberta/Em andamento/Fechada) e realizar consultas e
estatísticas básicas.
