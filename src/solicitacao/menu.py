from src.solicitacao.abrir import abrir_solicitacao
from src.solicitacao.editar import editar_status_solicitacao
from src.solicitacao.opcoes_consulta import opcoes_consultas_solicitacoes

def menu_solicitacao():
    print("\n--- Menu Solicitação ---")
    print("1: Abrir uma nova solicitação")
    print("2: Consultar solicitações")
    print("3: Editar status de uma solicitação")
    print("4: Sair")

def opcoes_solicitacao():
    continuar = True
    while continuar:
        menu_solicitacao()
        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
        except ValueError:
            print("Digite um número")
        else:
            if opcao == 1:
                abrir_solicitacao()
            elif opcao == 2:
                opcoes_consultas_solicitacoes()
            elif opcao == 3:
                editar_status_solicitacao()
            elif opcao == 4:
                print("Saindo...")
                continuar = False
            else:
                print("Número fora do escopo de opções.")
