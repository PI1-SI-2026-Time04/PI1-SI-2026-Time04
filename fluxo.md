Usuário → Menu Principal →

[1] Solicitante → CRUD de usuários  
[2] Solicitação → Criação de solicitações  
[3] Consultas → Filtros, status e estatísticas  
[4] Sair → Encerrar sistema  

→ Todas as ações interagem com o banco de dados MySQL  
→ O sistema opera em loop até o encerramento

## Fluxo Geral do Sistema

### 1. Inicialização

1. O sistema é iniciado a partir do arquivo `main.py`
2. A função principal é executada, iniciando o loop contínuo da aplicação
3. O menu principal é exibido ao usuário

---

### 2. Menu Principal

O sistema apresenta as opções:

- 1: Menu Solicitante
- 2: Menu Solicitação
- 3: Acompanhamento e Consultas
- 4: Sair

1. O usuário informa a opção desejada
2. O sistema valida a entrada:
   - Caso não seja numérica, solicita nova entrada
   - Caso inválida, informa erro

3. O sistema direciona o fluxo conforme a escolha

---

### 3. Fluxo do Menu Solicitante

1. O usuário acessa o módulo de solicitantes
2. O sistema permite:
   - Cadastro de solicitante
   - Edição de dados
   - Listagem de solicitantes
   - Remoção de solicitantes

3. As operações são validadas e persistidas no banco de dados
4. Após a execução, o sistema retorna ao menu principal

---

### 4. Fluxo do Menu Solicitação

1. O usuário acessa o módulo de solicitações
2. O sistema permite:
   - Criação de nova solicitação
   - Definição de categoria e prioridade
   - Associação a um solicitante

3. O sistema valida os dados informados
4. As informações são persistidas no banco de dados
5. O sistema retorna mensagem de confirmação
6. Após a execução, retorna ao menu principal

---

### 5. Fluxo de Acompanhamento e Consultas

#### 5.1 Acesso ao módulo

1. O usuário seleciona **"Acompanhamento e Consultas"**
2. O sistema exibe o menu do módulo

---

#### 5.2 Consulta e Listagem

1. O usuário seleciona **"Consultar solicitações"**
2. O sistema apresenta filtros:
   - Por Status
   - Por Prioridade
   - Por Usuário

3. O usuário escolhe o filtro
4. O sistema consulta o banco de dados MySQL
5. Exibe a lista contendo:
   - ID do solicitante
   - Categoria
   - Prioridade
   - Status
   - Data

6. Retorna ao menu do módulo

---

#### 5.3 Atualização de Status

1. O usuário seleciona **"Atualizar status"**
2. Informa o ID da solicitação
3. O sistema apresenta as opções:
   - 1: Aberta
   - 2: Em andamento
   - 3: Fechada

4. O usuário escolhe o novo status
5. O sistema valida:
   - Não permite alteração de solicitações fechadas

6. O sistema atualiza o status no banco de dados
7. Exibe confirmação de sucesso
8. Retorna ao menu do módulo

---

#### 5.4 Estatísticas

1. O usuário seleciona **"Ver estatísticas"**
2. O sistema realiza:
   - Contagem por status
   - Contagem por prioridade

3. Exibe os resultados ao usuário
4. Retorna ao menu do módulo

---

### 6. Encerramento

1. O usuário seleciona a opção **"Sair"**
2. O sistema finaliza a execução
