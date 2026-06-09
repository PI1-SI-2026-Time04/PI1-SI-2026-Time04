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
        SELECT id_solicitacao, categoria, prioridade, status
        FROM solicitacoes
        WHERE prioridade = %s
        ORDER BY data_abertura DESC
        """

        cursor.execute(sql, (prioridade,))
        resultados = cursor.fetchall()
        cursor.close()

        if not resultados:
            print("\nNenhuma solicitação encontrada.\n")
            return

        print(f"\n=== Solicitações {prioridade.upper()} ===\n")

        for linha in resultados:
            print(f"""ID: {linha[0]}
Categoria: {linha[1]}
Prioridade: {linha[2]}
Status: {linha[3]}
------------------------""")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar por prioridade: {erro}")
