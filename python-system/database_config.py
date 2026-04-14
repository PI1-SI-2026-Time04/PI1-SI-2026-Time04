import mysql.connector

def obtem_conexao():
    if obtem_conexao.conexao is None:
        obtem_conexao.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="projetointegrador"
        )
    return obtem_conexao.conexao

obtem_conexao.conexao = None