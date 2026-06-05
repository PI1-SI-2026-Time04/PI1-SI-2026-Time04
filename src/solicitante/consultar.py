import mysql.connector
from database_config import obtem_conexao

def consultar_solicitante():
    print("--- Listagem de solicitantes ---")

    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        sql = "SELECT * FROM solicitantes"
        cursor.execute(sql)

        # Recuperando os dados do cursor
        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhum registro encontrado.")
        else:
            for linha in resultados:
                print(f"ID: {linha[0]} | Nome: {linha[1]} | Email: {linha[2]} | Celular: {linha[3]}")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar dados: {erro}")
