import sqlite3 as conector


def inserir_dados():
#abertura da conexão
    try:
        conexao = conector.connect('meubanco.db')
        cursor = conexao.cursor()

        comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                VALUES (12345678900, 'Joao', '2000-01-01', 1);'''

        cursor.execute(comando)

        conexao.commit()

    except conexao.Error as Err:
        print('Erro inesperado:', Err)

    finally:
        if conexao:
            print('Transação bem sucedida')
            cursor.close()
            conexao.close()

if __name__ == '__main__':
    inserir_dados()
 