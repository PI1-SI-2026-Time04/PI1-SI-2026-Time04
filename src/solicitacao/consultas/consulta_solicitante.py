import mysql.connector
from database_config import obtem_conexao


def consultar_por_solicitante():
    try:
        id_solicitante = int(input("Digite o ID do solicitante: "))

        conexao = obtem_conexao()
        cursor = conexao.cursor()

        sql = """
        SELECT s.id_solicitacao,
               sol.nome,
               s.categoria,
               s.prioridade,
               s.status,
               s.data_abertura
        FROM solicitacoes s
        JOIN solicitantes sol
            ON s.id_usuario = sol.id_usuario
        WHERE s.id_usuario = %s
        ORDER BY s.data_abertura DESC
        """

        valores = (id_solicitante,)
        cursor.execute(sql, valores)
        resultados = cursor.fetchall()
        cursor.close()

        if not resultados:
            print("\nNenhuma solicitação encontrada.\n")
            return

        print("\n=== Solicitações do Solicitante ===\n")

        for linha in resultados:
            print(f"""ID Solicitação: {linha[0]}
Solicitante: {linha[1]}
Categoria: {linha[2]}
Prioridade: {linha[3]}
Status: {linha[4]}
Data: {linha[5]}
--------------------------""")

    except ValueError:
        print("Digite um ID válido.")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar por solicitante: {erro}")
