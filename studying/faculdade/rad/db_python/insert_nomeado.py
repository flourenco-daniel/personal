import sqlite3 as conector
from modelo import Pessoa

def insert_dinamico():
    conexao = conector.connect('meubanco.db')
    cursor = conexao.cursor()

    pessoa = Pessoa(54983254741,'Jose','1990-24-31', False)

    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
    
    #nesse exemplo, executarei a query em dict. Isso facilita quando não se sabe ao certo a ordem das colunas no BD    
    cursor.execute(comando, {"cpf": pessoa.cpf,
                             "nome": pessoa.nome,
                             "data_nascimento": pessoa.data_nascimento,
                             "usa_oculos": pessoa.usa_oculos})
    conexao.commit()

    cursor.close()
    conexao.close()


def exemplo_vars():
    
    conexao = conector.connect('meubanco.db')
    cursor = conexao.cursor()
    pessoa = Pessoa(74926738932,'Paulo','1960-12-25', True)
    comando = '''INSERT INTO Pessoa VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''

    cursor.execute(comando, vars(pessoa)) #o vars puxou os atributos da classe pessoa
    print(vars(pessoa))

    # Efetivação do comando
    conexao.commit()

    # Fechamento das conexões
    cursor.close()
    conexao.close()

exemplo_vars()

