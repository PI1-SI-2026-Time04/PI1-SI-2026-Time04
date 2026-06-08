# Fluxo do Sistema

## Visão Geral

O sistema tem como objetivo gerenciar solicitantes e solicitações, permitindo cadastro, consulta, atualização de status e geração de estatísticas.

Todas as operações realizadas pelos módulos interagem diretamente com o banco de dados **MySQL**.

O sistema permanece em execução em um loop contínuo até que o usuário escolha a opção de saída.

---

# Estrutura Geral de Navegação

```text
Usuário
   │
   ▼
Menu Principal
   │
   ├── Menu Solicitante
   │      ├── Cadastrar Solicitante
   │      ├── Consultar Solicitantes
   │      ├── Editar Solicitante
   │      ├── Excluir Solicitante
   │      └── Sair
   │
   ├── Menu Solicitação
   │      ├── Abrir Nova Solicitação
   │      ├── Consultar Solicitações
   │      │      ├── Consultar todas
   │      │      ├── Consultar por status
   │      │      ├── Consultar por prioridade
   │      │      ├── Consultar por solicitante
   │      │      └── Sair
   │      ├── Editar Status da Solicitação
   │      └── Sair
   │
   ├── Menu Estatísticas
   │      ├── Total de Solicitações
   │      ├── Total Solicitações por Status
   │      ├── Total Solicitações por Prioridade
   │      └── Sair
   │
   └── Encerrar Sistema
```

---

# 1. Inicialização do Sistema

1. O sistema é iniciado através do arquivo `main.py`.
2. A função `opcoes_principal()` é executada.
3. O loop principal da aplicação é iniciado.
4. O Menu Principal é apresentado ao usuário.

> **Nota:** A conexão com o banco de dados MySQL é estabelecida **sob demanda** (lazy), quando alguma operação chama `obtem_conexao()` em `database_config.py`. Não há conexão explícita na inicialização.

---

# 2. Menu Principal

O sistema exibe as seguintes opções:

| Opção | Descrição         |
| ----- | ----------------- |
| 1     | Menu Solicitante  |
| 2     | Menu Solicitação  |
| 3     | Menu Estatísticas |
| 4     | Sair              |

## Fluxo

1. O usuário informa a opção desejada.

2. O sistema valida a entrada:

   * Deve ser numérica;
   * Deve existir no menu.

3. Caso a opção seja inválida:

   * Exibe mensagem de erro;
   * Solicita nova entrada.

4. Caso válida:

   * Direciona para o módulo correspondente.

---

# 3. Menu Solicitante

## Opções Disponíveis

| Opção | Descrição                  |
| ----- | -------------------------- |
| 1     | Cadastrar novo solicitante |
| 2     | Consultar solicitantes     |
| 3     | Editar solicitante         |
| 4     | Excluir solicitante        |
| 5     | Sair                       |

---

## 3.1 Cadastrar Solicitante

1. O usuário seleciona **Cadastrar novo solicitante**.
2. O sistema solicita os dados:

   * **Nome** — apenas letras (espaços permitidos);
   * **E-mail** — formato válido e não duplicado no banco;
   * **Celular** — exatamente 11 dígitos numéricos.

3. Realiza validações dos campos obrigatórios (loop até entrada válida).
4. Salva os dados na tabela `solicitantes`.
5. Exibe mensagem de sucesso.
6. Retorna ao Menu Solicitante.

---

## 3.2 Consultar Solicitantes

1. O usuário seleciona **Consultar solicitantes**.
2. O sistema busca todos os registros na tabela `solicitantes`.
3. Exibe a listagem com: ID, Nome, E-mail e Celular.
4. Caso não haja registros, exibe mensagem informativa.
5. Retorna ao Menu Solicitante.

---

## 3.3 Editar Solicitante

1. O usuário informa o **ID** do solicitante.
2. O sistema verifica sua existência.
3. Caso não encontrado, exibe mensagem e encerra a operação.
4. Caso encontrado, exibe os dados atuais e apresenta submenu:

| Opção | Campo    |
| ----- | -------- |
| 1     | Nome     |
| 2     | E-mail   |
| 3     | Celular  |
| 4     | Sair     |

5. O usuário escolhe qual campo alterar.
6. O sistema solicita o novo valor (com validação para nome e celular).
7. Atualiza o campo escolhido no banco de dados.
8. Exibe confirmação da alteração.
9. Retorna ao submenu de edição (até o usuário escolher Sair).
10. Retorna ao Menu Solicitante.

---

## 3.4 Excluir Solicitante

1. O usuário informa o **ID** do solicitante.
2. O sistema verifica sua existência.
3. Caso não encontrado, exibe mensagem e encerra a operação.
4. Caso encontrado, exibe os dados atuais.
5. Solicita confirmação da exclusão (**S/N**).
6. Se confirmado (**S**), remove o registro do banco de dados.
7. Se cancelado (**N**), exibe mensagem de cancelamento.
8. Retorna ao Menu Solicitante.

---

# 4. Menu Solicitação

## Opções Disponíveis

| Opção | Descrição                    |
| ----- | ---------------------------- |
| 1     | Abrir nova solicitação       |
| 2     | Consultar solicitações       |
| 3     | Editar status da solicitação |
| 4     | Sair                         |

---

## 4.1 Abrir Nova Solicitação

1. O usuário seleciona **Abrir nova solicitação**.

2. O sistema solicita:

   * **ID do solicitante** — deve existir na tabela `solicitantes`;
   * **Categoria** — escolha numérica:

     | Opção | Categoria                        |
     | ----- | -------------------------------- |
     | 1     | Suporte de TI                    |
     | 2     | Manutenção Predial               |
     | 3     | Suprimentos / Almoxarifado       |
     | 4     | Recursos Humanos (RH)            |
     | 5     | Serviços Administrativos         |

   * **Descrição** — não pode ser vazia e deve ter no mínimo 10 caracteres;
   * **Urgência** — 1 (Baixa), 2 (Média) ou 3 (Alta);
   * **Impacto** — 1 (Pequeno), 2 (Moderado) ou 3 (Grande).

3. O sistema valida os dados informados.

4. A **prioridade é calculada automaticamente** com base na soma de urgência + impacto:

   | Soma (urgência + impacto) | Prioridade |
   | ------------------------- | ---------- |
   | 2 ou 3                    | Baixa      |
   | 4 ou 5                    | Média      |
   | 6                         | Alta       |

5. Cria a solicitação com status inicial **Aberta** (default do banco).

6. Salva os dados na tabela `solicitacoes`.

7. Exibe mensagem de confirmação com a prioridade calculada.

8. Retorna ao Menu Solicitação.

> **Nota:** A tabela `log_prioridade` existe no schema do banco, mas o registro de log ainda **não está implementado** no fluxo de abertura.

---

## 4.2 Consultar Solicitações

Ao selecionar esta opção, o sistema apresenta o submenu:

| Opção | Descrição                       |
| ----- | ------------------------------- |
| 1     | Consultar todas as solicitações |
| 2     | Consultar por status            |
| 3     | Consultar por prioridade        |
| 4     | Consultar por solicitante       |
| 5     | Sair                            |

### Consultar Todas as Solicitações

1. O sistema busca todas as solicitações cadastradas.
2. Exibe: ID da Solicitação, ID do Solicitante, Categoria (código numérico), Descrição, Urgência, Impacto, Prioridade, Status e Data de Abertura.
3. Retorna ao submenu **Consultar Solicitações**.

### Consultar por Status

1. O usuário informa o status desejado (Aberta, Em andamento ou Fechada).
2. O sistema realiza a consulta com JOIN na tabela de solicitantes.
3. Exibe: ID da Solicitação, Nome do Solicitante, Categoria, Prioridade, Status e Data de Abertura.
4. Retorna ao submenu **Consultar Solicitações**.

### Consultar por Prioridade

1. O usuário informa a prioridade desejada (Baixa, Média ou Alta).
2. O sistema realiza a consulta.
3. Exibe: ID da Solicitação, Categoria, Prioridade e Status.
4. Retorna ao submenu **Consultar Solicitações**.

### Consultar por Solicitante

1. O usuário informa o **ID** do solicitante.
2. O sistema realiza a consulta com JOIN na tabela de solicitantes.
3. Exibe: ID da Solicitação, Nome do Solicitante, Categoria, Prioridade, Status e Data de Abertura.
4. Retorna ao submenu **Consultar Solicitações**.

### Retorno ao Menu Solicitação

Após escolher **Sair** (opção 5) no submenu de consultas, o sistema retorna ao **Menu Solicitação**.

---

## 4.3 Editar Status da Solicitação

1. O usuário seleciona **Editar status da solicitação**.
2. Informa o **ID** da solicitação.
3. O sistema verifica se a solicitação existe.
4. Caso não exista, solicita novo ID.
5. Caso exista e esteja **Fechada**, informa que não é possível alterar e solicita outro ID.
6. Caso exista e não esteja fechada, exibe o status atual e apresenta as opções:

| Código | Status       |
| ------ | ------------ |
| 1      | Em andamento |
| 2      | Fechada      |

7. O usuário escolhe o novo status.
8. O sistema valida a alteração.
9. Solicitações **fechadas não podem ser reabertas**.
10. Atualiza o status no banco de dados.
11. Exibe confirmação da atualização.
12. Retorna ao Menu Solicitação.

---

# 5. Menu Estatísticas

## Opções Disponíveis

| Opção | Descrição             |
| ----- | --------------------- |
| 1     | Total de solicitações |
| 2     | Total por status      |
| 3     | Total por prioridade  |
| 4     | Sair                  |

---

## 5.1 Total de Solicitações

1. O sistema realiza a contagem geral das solicitações (`COUNT(*)`).
2. Exibe o total encontrado.
3. Retorna ao Menu Estatísticas.

---

## 5.2 Total por Status

1. O sistema agrupa as solicitações por status (`GROUP BY status`).
2. Exibe os quantitativos de cada status encontrado (ex.: Abertas, Em andamento, Fechadas).
3. Retorna ao Menu Estatísticas.

---

## 5.3 Total por Prioridade

1. O sistema agrupa as solicitações por prioridade (`GROUP BY prioridade`).
2. Exibe os quantitativos encontrados (Baixa, Média, Alta).
3. Retorna ao Menu Estatísticas.

---

# 6. Integração com Banco de Dados

Todas as funcionalidades realizam operações no banco de dados MySQL:

* Inserção de solicitantes;
* Consulta de solicitantes;
* Atualização de solicitantes;
* Exclusão de solicitantes;
* Abertura de solicitações;
* Consulta de solicitações;
* Atualização de status;
* Geração de estatísticas.

A conexão é gerenciada por `database_config.obtem_conexao()`, que reutiliza uma única conexão durante a execução.

As operações utilizam tratamento de exceções (`mysql.connector.Error`) para garantir a integridade dos dados e a estabilidade do sistema.

### Tabelas utilizadas

| Tabela           | Uso no sistema                                      |
| ---------------- | --------------------------------------------------- |
| `solicitantes`   | CRUD de solicitantes                                |
| `solicitacoes`   | Abertura, consultas, edição de status, estatísticas |
| `log_prioridade` | Definida no schema; **ainda não utilizada no código** |

---

# 7. Encerramento do Sistema

1. O usuário seleciona a opção **Sair** no Menu Principal (opção 4).
2. O sistema encerra o loop principal.
3. A aplicação é encerrada.

> **Nota:** Atualmente o sistema **não fecha explicitamente** a conexão com o banco ao encerrar. A conexão é encerrada automaticamente pelo runtime ao finalizar o processo.
