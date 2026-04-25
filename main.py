from solicitante.menu import opcoes_solicitante

def menu_principal():
    print("\n=== Sistema de Controle de Solicitações Corporativas ===")
    print("1: Menu Solicitante")
    print("2: Menu Solicitação")
    print("3: Menu Acompanhamento e Consultas")
    print("4: Sair")

def opcoes():
    continuar = True
    while continuar:
        menu_principal()
        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
        except ValueError:
            print("Digite um número.")
        else:
            if opcao == 1:
                opcoes_solicitante()
            elif opcao == 2:
                print("Em desenvolvimento...")
            elif opcao == 3:
                print("Em desenvolvimento...")
            elif opcao == 4:
                print("Saindo...")
                continuar = False
            else:
                print("Número fora do escopo de opções.")

opcoes()
