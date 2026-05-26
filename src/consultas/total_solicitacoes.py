import mysql.connector
from database_config import obtem_conexao

def total_solicitacoes():
    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        sql = "SELECT COUNT(*) FROM solicitacoes"
        cursor.execute(sql)

        resultado = cursor.fetchone()

        if not resultado:
            print("Nenhuma solicitação registrada.")
        else:
            print(f"\nTotal de solicitações: {resultado[0]}")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar dados: {erro}")
