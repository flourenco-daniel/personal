import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pedidos_ntl',
    allow_local_infile=True
)

cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS pedidos (
    Pedido INT,
    Pedido_ERP INT,
    Origem VARCHAR(255),
    Status VARCHAR(255),
    Status_Data DATE,
    Data_Programada DATE,
    Data_do_pedido DATE,
    Dia_do_pedido DATE,
    Data_de_Cadastro DATE,
    Nome VARCHAR(255),
    Sobrenome VARCHAR(255),
    CPF VARCHAR(18),
    CNPJ VARCHAR(18),
    Telefone VARCHAR(20),
    Celular VARCHAR(20),
    Email VARCHAR(255),
    CEP VARCHAR(10),
    Endereco VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(255),
    Cidade VARCHAR(255),
    Estado VARCHAR(2),
    CEP_de_Entrega VARCHAR(10),
    Endereco_de_Entrega VARCHAR(255),
    Numero_1 VARCHAR(10),
    Complemento_1 VARCHAR(255),
    Bairro_1 VARCHAR(255),
    Cidade_1 VARCHAR(255),
    Estado_1 VARCHAR(2),
    Quantidade_de_Itens INT,
    Sub_Total DECIMAL(10, 2),
    Cupom VARCHAR(255),
    Valor_Descontos DECIMAL(10, 2),
    Valor_Frete DECIMAL(10, 2),
    Valor_Total DECIMAL(10, 2),
    Forma_de_Entrega VARCHAR(255),
    Forma_de_Pagamento VARCHAR(255),
    Data_Pagamento DATE,
    Parcelas INT,
    Codigo_da_Transacao VARCHAR(255)
);
"""

load_data_query = """
LOAD DATA LOCAL INFILE 'C:/Users/danie/Documents/Python Scripts/db_naturallis/pedidos_ntl.csv'
INTO TABLE pedidos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    `Pedido`,
    `Pedido_ERP`,
    `Origem`,
    `Status`,
    `Status_Data`,
    `Data_Programada`,
    `Data_do_pedido`,
    `Dia_do_pedido`,
    `Data_de_Cadastro`,
    `Nome`,
    `Sobrenome`,
    `CPF`,
    `CNPJ`,
    `Telefone`,
    `Celular`,
    `Email`,
    `CEP`,
    `Endereco`,
    `Numero`,
    `Complemento`,
    `Bairro`,
    `Cidade`,
    `Estado`,
    `CEP_de_Entrega`,
    `Endereco_de_Entrega`,
    `Numero_1`,
    `Complemento_1`,
    `Bairro_1`,
    `Cidade_1`,
    `Estado_1`,
    `Quantidade_de_Itens`,
    `Sub_Total`,
    `Cupom`,
    `Valor_Descontos`,
    `Valor_Frete`,
    `Valor_Total`,
    `Forma_de_Entrega`,
    `Forma_de_Pagamento`,
    `Data_Pagamento`,
    `Parcelas`,
    `Codigo_da_Transacao`
);
"""

try:
    cursor.execute(create_table_query)
    connection.commit()
    print("Table 'pedidos' created successfully.")

    cursor.execute(load_data_query)
    connection.commit()
    print("Data loaded successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    connection.close()
