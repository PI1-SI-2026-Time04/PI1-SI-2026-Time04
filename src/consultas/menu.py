from src.solicitante.consultar import consultar_solicitante
from src.solicitacao.opcoes_consulta import opcoes_consultas_solicitacoes

def menu_consultas():
    print("\n--- Menu Consultas ---")
    print("1: Listar solicitantes")
    print("2: Listar solicitações")
    print("3: Sair")

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
                consultar_solicitante()
            elif opcao == 2:
                opcoes_consultas_solicitacoes()
            elif opcao == 3:
                print("Saindo...")
                continuar = False
            else:
                print("Número fora do escopo de opções.")

