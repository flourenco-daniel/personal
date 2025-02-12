import sqlite3 as conector
from modelo import Pessoa

def insert_dinamico():
    conexao = conector.connect('meubanco.db')
    cursor = conexao.cursor()

    pessoa = Pessoa(32987654321,'Maria','1990-01-31', False)

    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                VALUES (?, ?, ?, ?);'''
    
    cursor.execute(comando, (pessoa.cpf,
                             pessoa.nome,
                             pessoa.data_nascimento,
                             pessoa.usa_oculos))
    conexao.commit()

    cursor.close()
    conexao.close()

if __name__ == '__main__':
    insert_dinamico()

