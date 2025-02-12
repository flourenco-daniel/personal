import sqlite3 as conector

def using_select():
    conexao = conector.connect('meubanco.db')
    cursor = conexao.cursor()

    comando = '''SELECT nome, oculos FROM pessoa'''
    cursor.execute(comando)

    registros = cursor.fetchall()
    print('Tipo retornado pelo fetchall()', type(registros))

    for registro in registros:
        print('Tipo:', type(registro), '- Conteúdo:',registro)

    cursor.close()
    conexao.close()

if __name__ == '__main__':
    using_select()
