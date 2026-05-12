import mysql.connector
from database_config import obtem_conexao

def abrir_solicitacao():
    print("\n--- Abertura de Solicitação ---")

    continuar_pedindo_id = True

    while continuar_pedindo_id:
        try:
            id_busca = int(input("Digite o ID do solicitante relacionado à solicitação: "))

        except ValueError:
            print("Digite um número.")

        else:
            conexao = obtem_conexao()
            cursor = conexao.cursor()

            # verifica se o id do solicitante existe
            sql_verifica = "SELECT * FROM solicitantes WHERE id_usuario = %s"
            cursor.execute(sql_verifica, (id_busca,))

            resultado = cursor.fetchone()

            if not resultado:
                print("O ID que você inseriu não existe. Tente novamente.")
            else:
                continuar_pedindo_id = False
                print("ID encontrado com sucesso!")
    

    # Validando categoria
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

    # Validando descrição
    continuar_pedindo_descricao = True
    while continuar_pedindo_descricao:
        descricao = input("\nDescreva a solicitação: ")

        if descricao == "":
            print("A descrição não pode ser vazia. ")
        elif len(descricao) < 10:
            print("Descreva melhor o problema.")
        else:
            continuar_pedindo_descricao = False

    # Validando urgência
    continuar_pedindo_urgencia = True
    while continuar_pedindo_urgencia:
        print("\n--- Urgência ---")
        print("1 - Baixa (Pode aguardar)")
        print("2 - Média (Requer atenção em breve)")
        print("3 - Alta (Resolução imediata)\n")
        try:
            urgencia = int(input("Digite o número da opção: "))
        except ValueError:
            print("Digite um número")
        else:
            if urgencia in (1, 2, 3):
                continuar_pedindo_urgencia = False 
            else:
                print("Número fora do escopo. Tente novamente")

    # Validando impacto
    continuar_pedindo_impacto = True
    while continuar_pedindo_impacto:
        print("\n--- Impacto ---")
        print("1 - Pequeno (Apenas um usuário/tarefa)")
        print("2 - Moderado (Um setor ou processo importante)")
        print("3 - Grande (Toda a empresa ou serviço crítico)\n")
        try:
            impacto = int(input("Digite o número da opção: "))
        except ValueError:
            print("Digite um número")
        else:
            if impacto in (1, 2, 3):
                continuar_pedindo_impacto = False
            else:
                print("Número fora do escopo. Tente novamente")

    try:
        conexao = obtem_conexao()
        cursor = conexao.cursor()

        sql = "SELECT * FROM solicitantes WHERE id_usuario = %s"
        valor = (id_busca,)

        cursor.execute(sql, valor)

        resultado = cursor.fetchone()

        if resultado is None:
            print("Solicitante não encontrado")
        else:
            # Query para inserir os dados no banco
            sql = "INSERT INTO solicitacoes (id_usuario, categoria, descricao, urgencia, impacto) VALUES (%s, %s, %s, %s, %s)"

            valores = (id_busca, categoria, descricao, urgencia, impacto)

            # Executando e salvando (commit)
            cursor.execute(sql, valores)
            conexao.commit()

            print("\nSolicitação aberta com sucesso")

    except mysql.connector.Error as erro:
        print(f"Falha ao inserir dados: {erro}")


        




    


