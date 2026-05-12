import mysql.connector
from database_config import obtem_conexao

def consultar_solicitacao():
    print("--- Listagem de solicitações ---")

    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        sql = "SELECT * FROM solicitacoes"
        cursor.execute(sql)

        # Recuperando os dados do cursor
        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhum registro encontrado.")
        else:
            for linha in resultados:
                print(f"ID Solicitação: {linha[0]} | ID Solicitante: {linha[1]} | Categoria: {linha[2]} | Descrição: {linha[3]} | Urgência: {linha[4]} | Impacto: {linha[5]} | Prioridade: {linha[6]} | Status: {linha[7]} | Data de abertura: {linha[8]}")

    except mysql.connector.Error as erro:
        print(f"Falha ao consultar dados: {erro}")