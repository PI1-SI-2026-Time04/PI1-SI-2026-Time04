from database_config import obtem_conexao

def listar_por_status():
    try:
        status = input(
            "Digite o status (Aberta, Em andamento ou Fechada): "
        ).strip().title()

        conexao = obtem_conexao()
        cursor = conexao.cursor()

        query = """
        SELECT s.id_solicitacao,
               u.nome,
               s.categoria,
               s.prioridade,
               s.status,
               s.data_abertura
        FROM solicitacoes s
        JOIN solicitantes u
            ON s.id_usuario = u.id_usuario
        WHERE s.status = %s
        ORDER BY s.data_abertura DESC
        """

        cursor.execute(query, (status,))
        resultados = cursor.fetchall()

        if not resultados:
            print("\nNenhuma solicitação encontrada.\n")
            return

        print(f"\n=== Solicitações - Status {status.upper()} ===\n")

        for row in resultados:
            print(f"""
ID Solicitação: {row[0]}
Solicitante: {row[1]}
Categoria: {row[2]}
Prioridade: {row[3]}
Status: {row[4]}
Data: {row[5]}
--------------------------
""")

    except Exception as e:
        print("Erro ao consultar status:", e)
