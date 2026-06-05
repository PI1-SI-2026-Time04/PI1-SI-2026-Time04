from src.consultas.total_solicitacoes import total_solicitacoes
from src.consultas.total_solicitacoes_status import total_solicitacoes_por_status
from src.consultas.total_solicitacoes_prioridade import total_solicitacoes_por_prioridade


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
                total_solicitacoes()
            elif opcao == 2:
                total_solicitacoes_por_status()
            elif opcao == 3:
                total_solicitacoes_por_prioridade()
            elif opcao == 4:
                print("Saindo...")
                continuar = False
            else:
                print("Número fora do escopo de opções.")

