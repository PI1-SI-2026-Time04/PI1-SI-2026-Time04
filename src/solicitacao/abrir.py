import mysql.connector
from database_config import obtem_conexao

def abrir_solicitacao():
    print("\n--- Abertura de Solicitação ---")

    continuar_pedindo_id = True

    while continuar_pedindo_id:
        try:
            id_solicitante = int(input("Digite o ID do solicitante relacionado à solicitação: "))

        except ValueError:
            print("Digite um número.")

        else:
            conexao = obtem_conexao()
            cursor = conexao.cursor(buffered=True)

            sql_verifica = "SELECT * FROM solicitantes WHERE id_usuario = %s"
            cursor.execute(sql_verifica, (id_solicitante,))

            resultado = cursor.fetchone()
            cursor.close()

            if not resultado:
                print("O ID que você inseriu não existe. Tente novamente.")
            else:
                continuar_pedindo_id = False
                print("ID encontrado com sucesso!")

    # Categoria
    continuar_pedindo_categoria = True

    while continuar_pedindo_categoria:
        print("\n--- Categoria da Solicitação ---")
        print("1: Suporte de TI")
        print("2: Manutenção Predial")
        print("3: Suprimentos / Almoxarifado")
        print("4: Recursos Humanos (RH)")
        print("5: Serviços Administrativos\n")

        try:
            categoria = int(input("Digite o número da categoria: "))

        except ValueError:
            print("Digite um número.")

        else:
            if categoria in (1, 2, 3, 4, 5):
                continuar_pedindo_categoria = False
            else:
                print("Número fora do escopo. Tente novamente")

    # Descrição
    continuar_pedindo_descricao = True

    while continuar_pedindo_descricao:
        descricao = input("\nDescreva a solicitação: ")

        if descricao == "":
            print("A descrição não pode ser vazia.")

        elif len(descricao) < 10:
            print("Descreva melhor o problema.")

        else:
            continuar_pedindo_descricao = False

    # Urgência
    continuar_pedindo_urgencia = True

    while continuar_pedindo_urgencia:
        print("\n--- Urgência ---")
        print("1 - Baixa")
        print("2 - Média")
        print("3 - Alta\n")

        try:
            urgencia = int(input("Digite o número da opção: "))

        except ValueError:
            print("Digite um número")

        else:
            if urgencia in (1, 2, 3):
                continuar_pedindo_urgencia = False
            else:
                print("Número fora do escopo. Tente novamente")

    # Impacto
    continuar_pedindo_impacto = True

    while continuar_pedindo_impacto:
        print("\n--- Impacto ---")
        print("1 - Pequeno")
        print("2 - Moderado")
        print("3 - Grande\n")

        try:
            impacto = int(input("Digite o número da opção: "))

        except ValueError:
            print("Digite um número")

        else:
            if impacto in (1, 2, 3):
                continuar_pedindo_impacto = False
            else:
                print("Número fora do escopo. Tente novamente")

    # =========================
    # Cálculo da prioridade automática
    # =========================

    soma = urgencia + impacto

    if soma <= 2:
        prioridade = "Baixa"

    elif soma <= 4:
        prioridade = "Média"

    else:
        prioridade = "Alta"

    print(f"\nPrioridade definida automaticamente: {prioridade}")

    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO solicitacoes
        (id_usuario, categoria, descricao, urgencia, impacto, prioridade)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            id_solicitante,
            categoria,
            descricao,
            urgencia,
            impacto,
            prioridade
        )

        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()

        print("\nSolicitação aberta com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Falha ao inserir dados: {erro}")