import mysql.connector
from database_config import obtem_conexao

def total_solicitacoes_por_prioridade():
    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        sql = """
        SELECT prioridade, COUNT(*) 
        FROM solicitacoes
        GROUP BY prioridade
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()
        cursor.close()

        print("\n--- Total de Solicitações por Prioridade ---")

        if not resultados:
            print("Nenhuma solicitação cadastrada.")

        else:
            for prioridade, total in resultados:
                print(f"Prioridade {prioridade}: {total} solicitação(ões)")
                
    except mysql.connector.Error as erro:
        print(f"Falha ao consultar dados: {erro}")
