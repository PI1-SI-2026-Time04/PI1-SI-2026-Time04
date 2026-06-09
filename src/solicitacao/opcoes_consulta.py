from src.solicitacao.consultas.consultar import consultar_solicitacao
from src.solicitacao.consultas.consulta_prioridade import consultar_por_prioridade
from src.solicitacao.consultas.consulta_status import consultar_por_status
from src.solicitacao.consultas.consulta_solicitante import consultar_por_solicitante

def menu_consultas_solicitacoes():
    print("\n--- Consultar Solicitações ---")
    print("1: Consultar todas as solicitações")
    print("2: Consultar por status")
    print("3: Consultar por prioridade")
    print("4: Consultar por solicitante")
    print("5: Sair")

def opcoes_consultas_solicitacoes():
    continuar = True

    while continuar:
        menu_consultas_solicitacoes()
        
        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
        except ValueError:
            print("Digite um número")
        else:
            if opcao == 1:
                consultar_solicitacao()
            elif opcao == 2:
                consultar_por_status()
            elif opcao == 3:
                consultar_por_prioridade()
            elif opcao == 4:
                consultar_por_solicitante()
            elif opcao == 5:
                print("Saindo...")
                continuar = False
            else:
                print("Número fora do escopo de opções.")
