from database_config import obtem_conexao

def listar_por_solicitante():
    try:
        id_usuario = int(input("Digite o ID do solicitante: "))

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
        WHERE s.id_usuario = %s
        ORDER BY s.data_abertura DESC
        """

        cursor.execute(query, (id_usuario,))
        resultados = cursor.fetchall()

        if not resultados:
            print("\nNenhuma solicitação encontrada.\n")
            return

        print(f"\n=== Solicitações do Solicitante ===\n")

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

    except ValueError:
        print("Digite um ID válido.")

    except Exception as e:
        print("Erro ao consultar:", e)

    finally:
        cursor.close()
        conexao.close()