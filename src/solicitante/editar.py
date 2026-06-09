import mysql.connector
from database_config import obtem_conexao


def editar_solicitante():
    print("\n--- Editar Solicitante ---")

    continuar_pedindo_id = True
    while continuar_pedindo_id:
        try:
            id_solicitante = int(input("Digite o ID do solicitante que deseja editar: "))
        except ValueError:
            print("Digite um número.")
        else:
            continuar_pedindo_id = False

    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor(buffered=True)

        sql = "SELECT * FROM solicitantes WHERE id_usuario = %s"
        valores = (id_solicitante,)

        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        if not resultado:
            print("Solicitante não encontrado")
        else:
            print("Dados atuais:", resultado, "\n")

            opcoes_edicao = True
            while opcoes_edicao:
                print("Qual campo deseja alterar? ")
                print("1: Nome")
                print("2: E-mail")
                print("3: Celular")
                print("4: Sair\n")

                try:
                    opcao_desejada = int(input("Digite o número da opção desejada: "))
                except ValueError:
                    print("Digite um número.")
                else:
                    if opcao_desejada == 1:
                        continuar_pedindo_nome = True

                        while continuar_pedindo_nome:
                            novo_nome = input("Digite o novo nome: ")

                            if not novo_nome.replace(" ", "").isalpha():
                                print("Nome inválido. Use apenas letras.")
                            else:
                                continuar_pedindo_nome = False

                        cursor.execute("""
                            UPDATE solicitantes
                            SET nome = %s
                            WHERE id_usuario = %s
                        """, (novo_nome, id_solicitante))

                        conexao.commit()
                        print("Nome atualizado com sucesso!\n")

                    elif opcao_desejada == 2:
                        novo_email = input("Digite o novo e-mail: ")

                        cursor.execute("""
                            SELECT id_usuario
                            FROM solicitantes
                            WHERE email = %s
                            AND id_usuario <> %s
                        """, (novo_email, id_solicitante))

                        if cursor.fetchone():
                            print("Este e-mail já está cadastrado para outro usuário.\n")
                        else:
                            cursor.execute("""
                                UPDATE solicitantes
                                SET email = %s
                                WHERE id_usuario = %s
                            """, (novo_email, id_solicitante))

                            conexao.commit()
                            print("E-mail atualizado com sucesso!\n")

                    elif opcao_desejada == 3:
                        continuar_pedindo_celular = True

                        while continuar_pedindo_celular:
                            novo_celular = input("Digite o novo número de celular: ")

                            if not novo_celular.isdigit():
                                print("Número de celular inválido. Digite apenas números.")
                            elif len(novo_celular) != 11:
                                print("Número inválido. Um celular deve ter 11 dígitos.")
                            else:
                                continuar_pedindo_celular = False

                        cursor.execute("""
                            SELECT id_usuario
                            FROM solicitantes
                            WHERE celular = %s
                            AND id_usuario <> %s
                        """, (novo_celular, id_solicitante))

                        if cursor.fetchone():
                            print("Este telefone já está cadastrado para outro usuário.\n")
                        else:
                            cursor.execute("""
                                UPDATE solicitantes
                                SET celular = %s
                                WHERE id_usuario = %s
                            """, (novo_celular, id_solicitante))

                            conexao.commit()
                            print("Número de celular atualizado com sucesso!\n")

                    elif opcao_desejada == 4:
                        opcoes_edicao = False

                    else:
                        print("Número fora da opção desejada.")

        cursor.close()

    except mysql.connector.Error as erro:
        print(f"Falha ao editar dados: {erro}")