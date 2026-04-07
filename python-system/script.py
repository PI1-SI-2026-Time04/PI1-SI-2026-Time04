print("Sistema de Controle de Solicitações Corporativas\n")
# Print de resumo de scsc


print("""1: Cadastro de Solicitante
2: Abertura de Solilitação
3: Acompanhamento e Consultas
4: Sair
""")

continuar = True

while continuar:
    try:
        opcao = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Digite um número")
    else:
        if opcao == 1:  # Cadastro de Solicitante
            print("Tela de Cadastro de Solicitante\n")
        elif opcao == 2:  # de Solicitante
            print("Tela de Abertura de Solicitação\n")
        elif opcao == 3:  # Acompanhamento e Consultas (nessa tela, haverá sub-telas)
            print("Tela de Acompanhamento e Consultas\n")
        elif opcao == 4:  # Sair
            continuar = False
        else:
            print("Número fora do escopo de opções. Tente novamente.")