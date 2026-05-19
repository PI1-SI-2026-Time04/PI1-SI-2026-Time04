import mysql.connector


# substitua as credenciais com o banco que você estiver utilizando
def obtem_conexao():
    if obtem_conexao.conexao is None:
        obtem_conexao.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="scsc_db"
        )
    return obtem_conexao.conexao

obtem_conexao.conexao = None