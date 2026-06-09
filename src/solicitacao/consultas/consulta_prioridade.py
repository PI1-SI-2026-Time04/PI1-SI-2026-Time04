import mysql.connector
from database_config import obtem_conexao


def consultar_por_prioridade():
    try:
        continuar_pedindo_prioridade = True
        while continuar_pedindo_prioridade:
            prioridade = input("Digite a prioridade (Baixa, Média ou Alta): ").title()

            if prioridade in ["Baixa", "Média", "Alta"]:
                continuar_pedindo_prioridade = False
            else:
                print("Prioridade inválida. Tente novamente.")

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
        WHERE s.prioridade = %s
        ORDER BY s.data_abertura DESC
        """

        cursor.execute(sql, [prioridade])
        resultados = cursor.fetchall()
        cursor.close()

        if not resultados:
            print("\nNenhuma solicitação encontrada.\n")
            return

        print(f"\n=== Solicitações {prioridade.upper()} ===\n")

        for linha in resultados:
            print(f"""ID Solicitação: {linha[0]}
Solicitante: {linha[1]}
Categoria: {linha[2]}
Prioridade: {linha[3]}
Status: {linha[4]}
Data: {linha[5]}
--------------------------""")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar por prioridade: {erro}")
