import sqlite3 as conector

#passo 1: abertura de conexao
conexao = conector.connect("URL SQLITE")

#passo 2: aquisição de um cursor
cursor = conexao.cursor()

#passo 3: execução dos comandos SQL
cursor.execute("SELECT *, WHERE...")
#metodo fetchall retorna um conjunto de registros (lista com objetos variados)
cursor.fetchall()

#caso você tenha feito alguma alteração no BD, é necessario commitar
conexao.commit()

#passo 5: fechar o cursor e a conexão (nessa ordem)
cursor.close()
conexao.close()