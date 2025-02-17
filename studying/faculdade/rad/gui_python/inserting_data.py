import psycopg2 as pg

def conectar():
    try:
        conn = pg.connect(
            host='localhost',
            port='5432',
            user='postgres',
            dbname='postgres',
            password='1221')
        return conn  # Return connection so it can be used in other functions
    
    except Exception as error:
        print(error)
        return None

def inserirDados(codigo, nome, preco):
    conn = conectar()
    
    if conn:
        try:
            cur = conn.cursor()
            postgres_insert_query = '''INSERT INTO Produtos ("codigo", "nome", "preco") 
                                       VALUES (%s, %s, %s)'''
            record_to_insert = (codigo, nome, preco)
            cur.execute(postgres_insert_query, record_to_insert)
            conn.commit()
            count = cur.rowcount
            print(count, "registro inserido com sucesso na tabela Produtos")
        
        except (Exception, pg.Error) as error:
            print("Falha ao inserir registros:", error)
        
        finally:
            cur.close()
            conn.close()
            print('A conexão foi fechada')
    else:
        print('Falha ao conectar ao banco de dados.')

inserirDados(123, 'Produto Exemplo', 29.99,
             432, 'Produto2', 23.99)