import mysql.connector
from database_config import obtem_conexao

def consultar_solicitacao():
    print("\n--- Listagem de todas as solicitações ---")

    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        # SQL atualizado com JOIN para obter o nome do solicitante e ORDER BY para ordenação decrescente por data
        sql = """
        SELECT s.id_solicitacao, 
               sol.nome, 
               s.categoria, 
               s.descricao, 
               s.urgencia, 
               s.impacto, 
               s.prioridade, 
               s.status, 
               s.data_abertura
        FROM solicitacoes s
        JOIN solicitantes sol ON s.id_usuario = sol.id_usuario
        ORDER BY s.data_abertura DESC
        """
        
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()

        if not resultados:
            print("\nNenhum registro encontrado.")
        else:
            for linha in resultados:
                print(f"""ID Solicitação: {linha[0]}
Solicitante: {linha[1]}
Categoria: {linha[2]}
Descrição: {linha[3]}
Urgência: {linha[4]}
Impacto: {linha[5]}
Prioridade: {linha[6]}
Status: {linha[7]}
Data de abertura: {linha[8]}
--------------------------""")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar dados: {erro}")
