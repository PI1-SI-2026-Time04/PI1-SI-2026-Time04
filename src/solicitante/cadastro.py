import mysql.connector
from database_config import obtem_conexao


def cadastro_solicitante():
    print("--- Cadastro de Solicitante ---")

    # Validando nome
    continuar_pedindo_nome = True
    while continuar_pedindo_nome:
        nome = input("Digite o nome: ")

        if not nome.replace(" ", "").isalpha():
            print("Nome inválido. Use apenas letras.")
        else:
            continuar_pedindo_nome = False

    # -------------------------=========================------------------------ #

    # precisamos validar o email
    email = input("Digite o email: ")

    # -------------------------=========================------------------------ #

    # Validando número de celular
    continuar_pedindo_celular = True

    while continuar_pedindo_celular:
        celular = input("Digite o número de celular: ")

        if not celular.isdigit():
            print("Número de celular inválido. Digite apenas números.")
        else:
            if len(celular) != 11:
                print("Número inválido. Um celular deve ter 11 digitos.")
            else:
                continuar_pedindo_celular = False

    try:
        # Abrindo a conexão
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        # Query para inserir os dados no banco
        sql = "INSERT INTO solicitantes (nome, email, celular) VALUES (%s, %s, %s)"
        valores = (nome, email, celular)

        # Executando e salvando (commit)
        cursor.execute(sql, valores)  # perceba que eu estou passando como parâmetro as 2 váriaveis acima
        conexao.commit()

        print("\nRegistro inserido com sucesso")


    except mysql.connector.Error as erro:
        print(f"Falha ao inserir usuário no banco {erro}")
