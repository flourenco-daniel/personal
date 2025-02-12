import sqlite3 as conector

def update_sql():

    try:
        conexao = conector.connect('meubanco.db')
        conexao.execute("PRAGMA foreign_keys = on") #configurar uma FK no banco de dados
        cursor = conexao.cursor()

        comando1 = '''UPDATE Pessoa SET oculos = 1;''' #perceba que não falei em qual linha quero que o oculos receba o update
        # cursor.execute(comando1)

        comando2 = '''UPDATE Pessoa SET oculos = ? WHERE nome='Maria';'''
        cursor.execute(comando2, (True,))
        conexao.commit()
    
    except conexao.Error as err:
        print("Erro inesperado:", err)
    
    finally:
        print("Transação realizada com sucesso")
        cursor.close()
        conexao.close()

update_sql()