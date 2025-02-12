import sqlite3 as conector


def tabela_pessoa():
    try:
        conexao = conector.connect("meubanco.db")
        cursor = conexao.cursor()
        

        comando = '''CREATE TABLE Pessoa (
                        cpf INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        nascimento DATE NOT NULL,
                        oculos BOOLEAN NOT NULL,
                        PRIMARY KEY (cpf)
                        );'''
        cursor.execute(comando)

        conexao.commit()

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        if conexao:
            cursor.close()
            conexao.close()


def tabela_marca():
    try:
        conexao = conector.connect("meubanco.db")
        cursor = conexao.cursor()
        

        comando = '''CREATE TABLE Marca (
                        id INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        sigla CHARACTER(2) NOT NULL,
                        PRIMARY KEY (id)
                        );'''
        cursor.execute(comando)

        conexao.commit()

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:

        if conexao:
            cursor.close()
            conexao.close()

def tabela_veiculos():
    try:
        conexao = conector.connect("meubanco.db")
        cursor = conexao.cursor()
        

        comando = '''CREATE TABLE Veiculo (
                        placa CHARACTER (7) NOT NULL,
                        ano INTEGER NOT NULL,
                        cor TEXT NOT NULL,
                        proprietario INTEGER NOT NULL,
                        marca INTEGER NOT NULL,
                        PRIMARY KEY (placa),
                        FOREIGN KEY(proprietario) REFERENCES Pessoas(CPF)
                        FOREIGN KEY(marca) REFERENCES Marca(id)
                        );'''
        cursor.execute(comando)

        conexao.commit()

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:

        if conexao:
            cursor.close()
            conexao.close()


