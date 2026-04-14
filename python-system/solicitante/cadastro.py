import mysql.connector
from database_config import obtem_conexao

def cadastro_solicitante():
    print("--- Cadastro de Solicitante ---")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    try:
        # Abrindo a conexão
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        # Query para inserir os dados no banco
        sql = "INSERT INTO solicitante (nome, email, telefone) VALUES (%s, %s, %s)"
        valores = (nome, email, telefone)

        # Executando e salvando (commit)
        cursor.execute(sql, valores) # perceba que eu estou passando como parâmetro as 2 váriaveis acima
        conexao.commit()

        print("\nRegistro inserido com sucesso")


    except mysql.connector.Error as erro:
        print(f"Falha ao inserior usuário no banco {erro}")
