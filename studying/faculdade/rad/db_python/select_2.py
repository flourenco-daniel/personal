import sqlite3 as conector
from modelo import Pessoa

def tipo_registro():
    try:
        conexao = conector.connect('meubanco.db')
        cursor = conexao.cursor()

        comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
        cursor.execute(comando, {'usa_oculos': True})

        registros = cursor.fetchall()
        for registro in registros:
            pessoa = Pessoa(*registro)
            print('cpf:', type(pessoa.cpf), pessoa.cpf)
            print('nome', type(pessoa.nome), pessoa.nome)
            print('nascimento', type(pessoa.data_nascimento), pessoa.data_nascimento)
            print('oculos', type(pessoa.usa_oculos), pessoa.usa_oculos)

    except conexao.Error as err:
        print('Erro inesperado', err)
    
    finally:
        cursor.close()
        conexao.close()

if __name__ == '__main__':
    tipo_registro()
