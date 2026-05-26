import mysql.connector
from database_config import obtem_conexao

def total_por_status():
    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        query = """
        SELECT status, COUNT(*)
        FROM solicitacoes
        GROUP BY status
        """

        cursor.execute(query)
        resultados = cursor.fetchall()

        if not resultados:
            print("\nNenhuma solicitação cadastrada.\n")
            return

        print("\n--- TOTAL DE SOLICITAÇÕES POR STATUS ---")

        for status, total in resultados:
            print(f"{status}: {total}")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar dados: {erro}")