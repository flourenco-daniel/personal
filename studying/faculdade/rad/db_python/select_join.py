import sqlite3 as conector
from modelo import Veiculos

conexao = conector.connect('meubanco.db')
cursor = conexao.cursor()

comando = '''SELECT 
                Veiculo.placa, Veiculo.ano, Veiculo.cor,
                Veiculo.motor, Veiculo.proprietario,
                Marca.nome FROM veiculo JOIN Marca ON Marca.id = Veiculo.marca;'''
cursor.execute(comando)

reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculos(*reg_veiculo)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

cursor.close()
conexao.close()