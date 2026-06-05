import mysql.connector
from database_config import obtem_conexao


def consultar_por_status():
    try:
        status = input(
            "Digite o status (Aberta, Em andamento ou Fechada): "
        ).strip().title()

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
        WHERE s.status = %s
        ORDER BY s.data_abertura DESC
        """

        cursor.execute(sql, (status,))
        resultados = cursor.fetchall()

        if not resultados:
            print("\nNenhuma solicitação encontrada.\n")
            return

        print(f"\n=== Solicitações - Status {status.upper()} ===\n")

        for linha in resultados:
            print(f"""
ID Solicitação: {linha[0]}
Solicitante: {linha[1]}
Categoria: {linha[2]}
Prioridade: {linha[3]}
Status: {linha[4]}
Data: {linha[5]}
--------------------------
""")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar por status: {erro}")
