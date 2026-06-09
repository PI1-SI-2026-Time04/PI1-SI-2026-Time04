import mysql.connector
from database_config import obtem_conexao


def excluir_solicitante():
    print("\n--- Excluir Solicitante ---")

    continuar_pedindo_id = True
    while continuar_pedindo_id:
        try:
            id_solicitante = int(input("Digite o ID do solicitante que deseja excluir: "))
        except ValueError:
            print("Digite um número.")
        else:
            continuar_pedindo_id = False

    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor(buffered=True)

        sql = "SELECT * FROM solicitantes WHERE id_usuario = %s"
        valores = [id_solicitante]

        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        if resultado is None:
            print("Solicitante não encontrado")
            cursor.close()
        else:
            print("Dados atuais:", resultado, "\n")

            confirmacao = input("Tem certeza que deseja excluir este solicitante? (S/N): ").upper()

            continuar_pedindo_confirmacao = True

            while continuar_pedindo_confirmacao:
                if confirmacao != "S" and confirmacao != "N":
                    print("Digite apenas S para sim e N para não. Tente novamente.")
                    confirmacao = input("(S/N): ").upper()
                else:
                    continuar_pedindo_confirmacao = False
            if confirmacao == "S":
                cursor.execute("DELETE FROM solicitantes WHERE id_usuario = %s", valores)
                conexao.commit()
                print("Solicitante excluído com sucesso.")
            elif confirmacao == "N":
                print("Exclusão cancelada.")

            cursor.close()


    except mysql.connector.Error as erro:
        print(f"Falha ao excluir solicitante: {erro}")
