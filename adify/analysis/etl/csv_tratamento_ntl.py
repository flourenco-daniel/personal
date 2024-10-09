import pandas as pd
import os

pasta = "C:\\Users\\danie\\Documents\\Python Scripts\\dados_ntl"

def clean_cel(cell):
    if pd.isnull(cell):
        return cell
    return "55" + str(cell).replace(" ", "").replace("(", "").replace(")", "").replace("-", "")

# Passo2: definiindo função para processar cada .csv dentro da pasta
def processar_csvs(pasta_csvs):
    for arquivo in os.listdir(pasta_csvs):
        if arquivo.endswith(".csv"):
            file_path = os.path.join(pasta_csvs, arquivo)
            df = pd.read_csv(file_path)
            
            # verifica se todas as colunas necessárias estao presentes
            colunas_necessarias = ['Nome', 'Sobrenome', 'Email', 'Celular']
            if all(coluna in df.columns for coluna in colunas_necessarias):
                df = df[colunas_necessarias]
                df['Celular'] = df['Celular'].apply(clean_cel)
                novo_nome_arquivo = arquivo.replace(".csv", "_final.csv")
                novo_path_arquivo = os.path.join(pasta_csvs, novo_nome_arquivo)
                df.to_csv(novo_path_arquivo, index=False)
                print(f"Deu bom. Tá salvo no {novo_path_arquivo}")
            else:
                print(f"Arquivo {arquivo} não possui todas as colunas necessárias. Pulando arquivo.")

# chama a função para processar os CSVs
processar_csvs(pasta)
