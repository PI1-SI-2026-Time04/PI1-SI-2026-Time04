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
