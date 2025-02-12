import sqlite3 as conector

#abertura da conexão
conexao = conector.connect("URLSQLITE")

#cursor - o cursor representa uma estrutura de controle para executar uma query retornando um dataset ou linhas específicas (linha a linha)
cursor = conexao.cursor()


cursor.execute('...')
cursor.fetchall

#efetivação do comando
conexao.commit()
#a partir daqui, os dados estão gravados no banco de dados

#fecha o cursor e conexão
cursor.close()
conexao.close()