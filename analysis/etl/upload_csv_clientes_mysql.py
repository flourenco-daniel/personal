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
CREATE TABLE IF NOT EXISTS clientes (
    Status VARCHAR(10),
    Data_de_Cadastro DATE,
    Nome VARCHAR(255),
    Sobrenome VARCHAR(255),
    SEXO VARCHAR(1),
    Email VARCHAR(255),
    CPF VARCHAR(18),
    Data_de_aniversario DATE,
    Telefone VARCHAR(20),
    Celular VARCHAR(20),
    CEP VARCHAR(10),
    Endereco VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(255),
    Estado VARCHAR(2),
    Cidade VARCHAR(255),
    Como_conheceu VARCHAR(255),
    Como_conheceu_texto VARCHAR(255),
    Instagram VARCHAR(255),
    Receber_news VARCHAR(255)
);
"""

try:
    cursor.execute(create_table_query)
    connection.commit()
    print("Table 'clientes' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

load_data_query = """
LOAD DATA LOCAL INFILE 'C:/Users/danie/Documents/Python Scripts/table_ntl_costumers.csv'
INTO TABLE clientes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    Status,
    Data_de_Cadastro,
    Nome,
    Sobrenome,
    SEXO,
    Email,
    CPF,
    Data_de_aniversario,
    Telefone,
    Celular,
    CEP,
    Endereco,
    Numero,
    Complemento,
    Bairro,
    Estado,
    Cidade,
    Como_conheceu,
    Como_conheceu_texto,
    Instagram,
    Receber_news
);
"""

try:
    cursor.execute(load_data_query)
    connection.commit()
    print("Data loaded successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    connection.close()