import sqlite3 as conector

def alterar_veiculos():
    try:
        conexao = conector.connect("meubanco.db")
        cursor = conexao.cursor()

        comando = '''ALTER TABLE Veiculo 
                        ADD motor REAL;'''
        
        cursor.execute(comando)

        conexao.commit()

    except conector.Error as err:
            print("Erro inesperado:", err)
    finally:
        if conexao:
            cursor.close()
            conexao.close()

alterar_veiculos()       