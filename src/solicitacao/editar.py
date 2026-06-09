import mysql.connector
from database_config import obtem_conexao


def atualizar_status_solicitacao(id_solicitacao, novo_status):
    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        # Verifica se a solicitação existe
        cursor.execute(
            "SELECT status FROM solicitacoes WHERE id_solicitacao = %s",
            (id_solicitacao,),
        )
        resultado = cursor.fetchone()

        if not resultado:
            cursor.close()
            print("Solicitação não encontrada.")
            return

        status_atual = resultado[0]

        # regra de integridade
        if status_atual == "Fechada":
            cursor.close()
            print("Não é possível alterar ou reabrir uma solicitação já fechada.")
            return

        # validação de status permitido
        status_validos = ["Aberta", "Em andamento", "Fechada"]

        if novo_status not in status_validos:
            cursor.close()
            print("Status inválido.")
            return

        # Atualiza o status
        sql = """
        UPDATE solicitacoes
        SET status = %s
        WHERE id_solicitacao = %s
        """

        cursor.execute(sql, (novo_status, id_solicitacao))
        conexao.commit()
        cursor.close()

        print("Status atualizado com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Falha ao atualizar status: {erro}")


def editar_status_solicitacao():
    print("\n--- Editar status da solicitação ---")

    id_solicitacao = None
    continuar_pedindo_id = True

    while continuar_pedindo_id:
        try:
            id_informado = int(input("Digite o ID da solicitação que deseja editar: "))
        except ValueError:
            print("Digite um número.")
        else:
            try:
                conexao = obtem_conexao()
                cursor = conexao.cursor(buffered=True)
                cursor.execute(
                    "SELECT id_solicitacao, status FROM solicitacoes WHERE id_solicitacao = %s",
                    (id_informado,),
                )
                resultado = cursor.fetchone()

                if not resultado:
                    cursor.close()
                    print("O ID que você inseriu não existe. Tente novamente.")
                else:
                    status_atual = resultado[1]
                    print(f"Solicitação encontrada. Status atual: {status_atual}")
                    if status_atual == "Fechada":
                        print(
                            "Não é possível alterar ou reabrir uma solicitação já fechada. "
                            "Digite outro ID."
                        )
                    else:
                        continuar_pedindo_id = False
                        id_solicitacao = id_informado
            except mysql.connector.Error as erro:
                print(f"Falha ao consultar dados: {erro}")

    novo_status = None
    continuar_escolhendo_status = True

    while continuar_escolhendo_status:
        print("\n--- Novo status ---")
        print("1: Em andamento")
        print("2: Fechada\n")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Digite um número.")
        else:
            if opcao == 1:
                novo_status = "Em andamento"
                continuar_escolhendo_status = False
            elif opcao == 2:
                novo_status = "Fechada"
                continuar_escolhendo_status = False
            else:
                print("Número fora do escopo de opções.")

    atualizar_status_solicitacao(id_solicitacao, novo_status)
