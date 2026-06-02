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
2. A função principal é executada.
3. É estabelecida a conexão com o banco de dados MySQL.
4. O loop principal da aplicação é iniciado.
5. O Menu Principal é apresentado ao usuário.

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
2. O sistema solicita os dados necessários.
3. Realiza validações dos campos obrigatórios.
4. Salva os dados no banco de dados.
5. Exibe mensagem de sucesso.
6. Retorna ao Menu Solicitante.

---

## 3.2 Consultar Solicitantes

1. O usuário seleciona **Consultar solicitantes**.
2. O sistema busca os registros cadastrados.
3. Exibe a listagem dos solicitantes.
4. Retorna ao Menu Solicitante.

---

## 3.3 Editar Solicitante

1. O usuário informa o ID do solicitante.
2. O sistema verifica sua existência.
3. Solicita os novos dados.
4. Atualiza as informações no banco de dados.
5. Exibe confirmação da alteração.
6. Retorna ao Menu Solicitante.

---

## 3.4 Excluir Solicitante

1. O usuário informa o ID do solicitante.
2. O sistema verifica sua existência.
3. Solicita confirmação da exclusão.
4. Remove o registro do banco de dados.
5. Exibe mensagem de sucesso.
6. Retorna ao Menu Solicitante.

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

   * Solicitante;
   * Categoria;
   * Prioridade;
   * Descrição.

3. O sistema valida os dados informados.

4. Cria a solicitação com status inicial **Aberta**.

5. Salva os dados no banco de dados.

6. Exibe mensagem de confirmação.

7. Retorna ao Menu Solicitação.

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
2. Exibe os resultados encontrados.

### Consultar por Status

1. O usuário informa o status desejado.
2. O sistema realiza a consulta.
3. Exibe os resultados encontrados.

### Consultar por Prioridade

1. O usuário informa a prioridade desejada.
2. O sistema realiza a consulta.
3. Exibe os resultados encontrados.

### Consultar por Solicitante

1. O usuário informa o solicitante.
2. O sistema realiza a consulta.
3. Exibe as solicitações relacionadas.

### Dados Exibidos

* ID da Solicitação
* ID do Solicitante
* Categoria
* Prioridade
* Status
* Data de Abertura

Após qualquer consulta, o sistema retorna ao Menu Solicitação.

---

## 4.3 Editar Status da Solicitação

1. O usuário seleciona **Editar status da solicitação**.
2. Informa o ID da solicitação.
3. O sistema verifica se a solicitação existe.
4. Exibe as opções:

| Código | Status       |
| ------ | ------------ |
| 1      | Aberta       |
| 2      | Em andamento |
| 3      | Fechada      |

5. O usuário escolhe o novo status.
6. O sistema valida a alteração.
7. Solicitações fechadas não podem ser reabertas.
8. Atualiza o status no banco de dados.
9. Exibe confirmação da atualização.
10. Retorna ao Menu Solicitação.

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

1. O sistema realiza a contagem geral das solicitações.
2. Exibe o total encontrado.
3. Retorna ao Menu Estatísticas.

---

## 5.2 Total por Status

1. O sistema agrupa as solicitações por status.

2. Exibe os quantitativos de:

   * Abertas;
   * Em andamento;
   * Fechadas.

3. Retorna ao Menu Estatísticas.

---

## 5.3 Total por Prioridade

1. O sistema agrupa as solicitações por prioridade.
2. Exibe os quantitativos encontrados.
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

As operações devem utilizar tratamento de exceções para garantir a integridade dos dados e a estabilidade do sistema.

---

# 7. Encerramento do Sistema

1. O usuário seleciona a opção **Sair** no Menu Principal.
2. O sistema encerra o loop principal.
3. A conexão com o banco de dados é finalizada.
4. A aplicação é encerrada de forma segura.
