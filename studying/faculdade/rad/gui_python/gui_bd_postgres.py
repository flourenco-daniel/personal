import psycopg2 as pg

def conectar():
    try:
        conn = pg.connect(
            host = 'localhost',
            port = '5432',
            user = 'postgres',
            dbname = 'postgres',
            password = '1221')
        cur = conn.cursor()

        query = '''CREATE TABLE IF NOT EXISTS Produtos(
                    id SERIAL PRIMARY KEY,
                    codigo INT NOT NULL,
                    nome VARCHAR(100) NOT NULL,
                    preco DECIMAL (10,2) NOT NULL
                    )'''
        
        # cur.execute(query)
        # conn.commit()
        cur.execute('''SELECT * FROM Produtos''')
        registros = cur.fetchall
        for registro in registros:
            print(registro)

    except Exception as error:
        print(error)

    finally:
        cur.close()
        conn.close()
        print('Conexão efetuada com sucesso')

conectar()