import pandas as pd
import os

pasta = "C:\\Users\\danie\\Documents\\Python Scripts\\dados_ntl"

def colunas_csvs(pasta_csvs):
    for arquivo in os.listdir(pasta_csvs):
        if arquivo.endswith(".csv"):
            caminho_arquivo = os.path.join(pasta_csvs, arquivo)
            df = pd.read_csv(caminho_arquivo)
            colunas = df.columns.to_list()
            print ("Lista de colunas do arquivo:", arquivo," ",colunas)
        else:
            print ("Alguma coisa deu ruim!")

colunas_csvs(pasta)
