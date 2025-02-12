import sqlite3 as conector

def conectar_bando(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   preco REAL NOT NULL,
                   estoque INTEGER NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTES Clientes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cliente_id INTEGER NOT NULL,
                   produto_id INTEGER NOT NULL,
                   quantidade INTEGER NOT NULL,
                   data_pedido DATE NOT NULL,
                   FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                   FOREIGN KEY (produto_id) REFERENCES Produtos(id))''')
    conexao.commit()

def inserir_dados(conexao):
    cursor = conexao.cursor()
   
    produtos = [('Notebook', 2999.99, 10),
                ('Smartphone', 1999.99, 20),
                ('Tablet', 999.99, 30)]
   
    clientes = [('Alice', 'alice@example.com'),
                ('Bob', 'bob@example.com'),
                ('Charlie', 'charlie@example.com')]
   
    pedidos = [(1, 1, 2, '2023-06-15'),
               (2, 2, 1, '2023-06-16'),
               (3, 3, 3, '2023-06-17')]
   

    #o execute many diz que quero executar diversas instruções (já que são vários itens na lista de cada tabela)
    cursor.executemany('INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)
    cursor.executemany('INSERT INTO Clientes (nome, email) VALUES (?, ?)', clientes)
    cursor.executemany('INSERT INTO Pedidos (cliente_id, produto_id, quantidade, data_pedido) VALUES (?, ?, ?, ?)', pedidos)
   
    conexao.commit()

