from src.solicitante.menu import opcoes_solicitante
from src.solicitacao.menu import opcoes_solicitacao
from src.consultas.menu import opcoes_consultas

def menu_principal():
    print("\n=== Sistema de Controle de Solicitações Corporativas ===")
    print("1: Menu Solicitante")
    print("2: Menu Solicitação")
    print("3: Menu Estatísticas")
    print("4: Sair")

def opcoes_principal():
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
                opcoes_solicitacao()
            elif opcao == 3:
                opcoes_consultas()
            elif opcao == 4:
                print("Saindo...")
                continuar = False
            else:
                print("Número fora do escopo de opções.")


if __name__ == "__main__":
    opcoes_principal()
