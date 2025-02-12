import sqlite3 as connector

def drop_veiculos():
    try:
        conexao = connector.connect("meubanco.db")
        cursor = conexao.cursor()
    
        comando = ('''DROP TABLE Veiculo''')
        cursor.execute(comando)

        conexao.commit()
    
    except conexao.Error as err:
        print("Erro inesperado:", err)

    finally:
        if conexao:
            print("Transação bem sucedida")
            cursor.close()
            conexao.close()

drop_veiculos()

 