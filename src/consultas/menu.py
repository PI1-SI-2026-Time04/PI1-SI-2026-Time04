# puxem os imports aqui das funções de vocês

def menu_consultas():
    print("\n--- Estatísticas ---")
    print("1: Total de solicitações")
    print("2: Total de solicitações por status")
    print("3: Total de solicitações por prioridade")
    print("4: Sair")

def opcoes_consultas():
    continuar = True
    while continuar:
        menu_consultas()
        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
        except ValueError:
            print("Digite um número")
        else:
            if opcao == 1:
                print("Tarefa da Maria")
            elif opcao == 2:
                print("Tarefa da Anita")
            elif opcao == 3:
                print("Tarefa da Miguel")
            elif opcao == 4:
                print("Saindo...")
                continuar = False
            else:
                print("Número fora do escopo de opções.")

