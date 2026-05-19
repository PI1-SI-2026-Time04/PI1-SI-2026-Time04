from database_config import obtem_conexao

def listar_por_prioridade():
    try:
        prioridade = input(
            "Digite a prioridade (Baixa, Média ou Alta): "
        ).title()

        conexao = obtem_conexao()
        cursor = conexao.cursor()

        query = """
        SELECT id_solicitacao, categoria, prioridade, status
        FROM solicitacoes
        WHERE prioridade = %s
        ORDER BY data_abertura DESC
        """

        cursor.execute(query, (prioridade,))
        resultados = cursor.fetchall()

        if not resultados:
            print("\nNenhuma solicitação encontrada.\n")
            return

        print(f"\n=== Solicitações {prioridade.upper()} ===\n")

        for row in resultados:
            print(f"""
ID: {row[0]}
Categoria: {row[1]}
Prioridade: {row[2]}
Status: {row[3]}
------------------------
""")

    except Exception as e:
        print("Erro:", e)
