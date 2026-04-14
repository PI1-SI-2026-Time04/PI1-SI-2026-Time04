import mysql.connector
from database_config import obtem_conexao

from solicitante.cadastro import cadastro_solicitante
from solicitante.consultar import consultar_solicitante
from solicitante.editar import editar_solicitante
from solicitante.excluir import excluir_solicitante

def menu_solicitante():
    print("--- Menu Solicitante ---")
    print("1: Cadastrar")
    print("2: Consultar")
    print("3: Editar")
    print("4: Excluir")
    print("5: Sair")

def opcoes_solicitante():
    continuar = True
    while continuar:
        try:
            opcao = int(input("\nDigite o número da opção opção desejada: "))
        except ValueError:
            print("Digite um número")
        else:
            if opcao == 1:
                cadastro_solicitante()
            elif opcao == 2:
                consultar_solicitante()
            elif opcao == 3:
                editar_solicitante()
            elif opcao == 4:
                excluir_solicitante()
            elif opcao == 5:
                continuar = False
            else:
                print("Número fora do escopo de opções.")