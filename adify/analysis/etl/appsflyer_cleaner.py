import pandas as pd
import json

# Caminho para o arquivo CSV a ser tratado
caminho_arquivo = 'C:\\Users\\Daniel\\Desktop\\raw_data.csv'

# Função para processar cada linha do CSV e extrair os dados do JSON
def processar_linha(row):
    try:
        # Carregar a string JSON da coluna 'Event Value'
        data = json.loads(row['Event Value'])
        
        # Criar um dicionário para armazenar os dados processados
        dados_processados = {}
        
        # Iterar sobre cada chave e valor do objeto JSON
        for chave, valor in data.items():
            # Armazenar o valor no dicionário, tratando valores ausentes como None
            dados_processados[chave] = valor if valor is not None else None
        
        return pd.Series(dados_processados)  # Retornar como Series para formar o DataFrame
    
    except json.JSONDecodeError:
        return pd.Series({})  # Retornar uma Series vazia em caso de erro na decodificação JSON

# Carregar o arquivo CSV e aplicar a função de processamento em cada linha
dataframe_event_value = pd.read_csv(caminho_arquivo).apply(processar_linha, axis=1)

# Exibir o DataFrame resultante com os dados processados
print(dataframe_event_value.head())
new_dir = 'C:\\Users\\Daniel\\Desktop\\data_cleaned.csv'

dataframe_event_value.to_csv(new_dir, index=False)