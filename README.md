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

- RF01 – Cadastro de Solicitante
Cadastrar e listar solicitantes com validação básica de dados.

| Campo               | Descrição                              | Obrigatório |
|--------------------|------------------------------------------|-------------|
| Usuário            | Nome de usuário para acesso ao sistema   | Sim         |
| Senha              | Senha de autenticação do usuário         | Sim         |
| Email              | Email válido do solicitante              | Sim         |
| Departamento       | Departamento ao qual o usuário pertence  | Sim         |
| Telefone           | Número de telefone para contato          | Não         |
| Data de Nascimento | Data de nascimento do solicitante        | Não         |
  
- RF02 – Abertura de Solicitação
Registrar solicitação vinculada ao solicitante, contendo tipo/categoria, descrição, data/hora
e status inicial.
- RF03 – Prioridade Automática
Definir regra objetiva para cálculo automático de prioridade (Baixa/Média/Alta) e
armazenar no banco.
- RF04 – Acompanhamento e Consultas
Permitir atualizar status (Aberta/Em andamento/Fechada) e realizar consultas e
estatísticas básicas.
