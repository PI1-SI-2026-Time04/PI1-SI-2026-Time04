from menu_solicitante import menu_solicitante, opcoes_solicitante


def menu_principal():
    print("\n=== Sistema de Controle de Solicitações Corporativas ===")
    print("1: Menu Solicitante")
    print("2: Menu Solicitação")
    print("3: Menu Acompanhamento e Consultas")
    print("4: Sair")

def opcoes():
    continuar = True
    while continuar:
        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
        except ValueError:
            print("Digite um número")
        else:
            if opcao == 1:
                menu_solicitante()
            elif opcao == 2:
                print("Em desenvolvimento...")
            elif opcao == 3:
                print("Em desenvolvimento...")
            elif opcao == 4:
                continuar = False
            else:
                print("Número fora do escopo de opções.")

menu_principal()
opcoes()




