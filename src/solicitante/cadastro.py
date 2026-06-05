import mysql.connector
from database_config import obtem_conexao
from email_validator import validate_email, EmailNotValidError


def cadastro_solicitante():
    print("\n--- Cadastro de Solicitante ---")

    # Validando nome
    continuar_pedindo_nome = True
    while continuar_pedindo_nome:
        nome = input("Digite o nome: ")

        if not nome.replace(" ", "").isalpha():
            print("Nome inválido. Use apenas letras.")
        else:
            continuar_pedindo_nome = False

    # -------------------------=========================------------------------ #

    continuar_pedindo_email = True

    while continuar_pedindo_email:
        email = input("Digite o email: ")

        try:
            # valida formato do email
            email_validado = validate_email(
                email,
                check_deliverability=False # estou dizendo para validar apenas o formato do email, sem considerar se o domínio realmente existe
            )

            # pega email normalizado
            email = email_validado.email

            conexao = obtem_conexao()
            cursor = conexao.cursor()

            # verifica se email já existe
            sql_verifica = "SELECT * FROM solicitantes WHERE email = %s"
            cursor.execute(sql_verifica, (email,))

            resultado = cursor.fetchone()

            if resultado:
                print("Este e-mail já está cadastrado. Tente novamente.")
            else:
                continuar_pedindo_email = False

        except EmailNotValidError as erro:
            print(f"Email inválido: {erro}")

        except mysql.connector.Error as erro:
            print(f"Erro ao verificar email: {erro}")

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

        print("\nSolicitante cadastrado com sucesso")


    except mysql.connector.Error as erro:
        print(f"Falha ao inserir solicitante no banco: {erro}")
