# Sistema de Controle de Solicitações Corporativas (SCSC)

O SCSC é uma aplicação CLI desenvolvida em Python para o gerenciamento centralizado de demandas internas. O sistema permite o cadastro de solicitantes, a abertura de chamados com classificação automática de prioridade, a atualização de status e a geração de estatísticas operacionais, utilizando MySQL para persistência de dados.

## Integrantes
- Anita Barbosa
- Ivan Henrique
- Maria Daon
- Miguel Souza

---

## 1. Arquitetura do Sistema
O projeto segue uma estrutura modular para facilitar a manutenção:
- `main.py`: Ponto de entrada que gerencia o menu principal.
- `src/solicitante/`: CRUD e gestão de usuários solicitantes.
- `src/solicitacao/`: Fluxos de abertura, edição e consultas de chamados.
- `src/consultas/`: Módulo dedicado a estatísticas e métricas de volume.
- `database_config.py`: Centraliza a configuração e conexão com o banco de dados via variáveis de ambiente.

---

## 2. Requisitos Funcionais (Documento de Visão)

### 3.1 Identificação de Usuário
- **Cadastro:** Coleta nome, e-mail e celular (11 dígitos).
- **Validações:** 
  - Nome aceita apenas letras e espaços.
  - E-mail validado por formato (RFC 5322) e unicidade no banco de dados.
  - Celular validado para conter apenas números e exatamente 11 dígitos.
- **Consulta/Exclusão:** Permite listar usuários e remover registros (com exclusão em cascata das solicitações vinculadas).

### 3.2 Registro de Solicitação
- **Vínculo:** Cada chamado deve obrigatoriamente estar associado a um ID de solicitante válido.
- **Categorias Fixas:** 
  1. Suporte de TI
  2. Manutenção Predial
  3. Suprimentos / Almoxarifado
  4. Recursos Humanos (RH)
  5. Serviços Administrativos
- **Validação de Descrição:** Mínimo de 10 caracteres obrigatórios.
- **Confirmação:** Ao finalizar, o sistema exibe o ID da solicitação gerado e a prioridade atribuída.

### 3.3 Classificação Automática de Prioridade
Calculada pela soma dos fatores de **Urgência (1-3)** e **Impacto (1-3)** informados na abertura:
- **Baixa:** Soma 2 ou 3.
- **Média:** Soma 4 ou 5.
- **Alta:** Soma 6.

### 3.4 Atualização de Status
- **Estados:** Aberta (inicial), Em andamento, Fechada.
- **Regra de Integridade:** Solicitações com status "Fechada" são bloqueadas para qualquer alteração posterior, garantindo a imutabilidade do histórico final.

### 3.5 Consultas e Listagens
- **Geral:** Lista todas as solicitações com JOIN para exibir o nome do solicitante e tradução da categoria numérica para texto, ordenada por data decrescente.
- **Filtros:** Consultas específicas por Status, Prioridade ou Solicitante.

### 3.6 Estatísticas Básicas
- Relatórios de volume total de chamados.
- Distribuição quantitativa agrupada por Status e por Prioridade.

---

## 3. Configuração do Banco de Dados
O sistema utiliza o banco `scsc_db` com as seguintes tabelas:
- `solicitantes`: `id_usuario`, `nome`, `email`, `celular`.
- `solicitacoes`: `id_solicitacao`, `id_usuario` (FK), `categoria`, `descricao`, `urgencia`, `impacto`, `prioridade`, `status`, `data_abertura`.

---

## 4. Instalação e Uso

### Requisitos
- Python 3.10+
- MySQL Server 8.0+

### Configuração Inicial
1. Execute o script `database/scsc.sql` no MySQL.
2. Crie um arquivo `.env` na raiz com:
   ```env
   DB_HOST=localhost
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_NAME=scsc_db
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie o sistema:
   ```bash
   python main.py
   ```
