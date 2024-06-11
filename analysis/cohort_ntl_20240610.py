import pandas as pd

df = pd.read_csv("C:\\Users\\danie\\Documents\\Python Scripts\\dados_ntl\\base_cohort.csv")
df['cpf'] = df['cpf'].apply(lambda x: '{:.0f}'.format(x))

df['Data_do_pedido'] = pd.to_datetime(df['Data_do_pedido'], format='%Y-%m-%d')

df['primeira_compra'] = pd.to_datetime(df['primeira_compra'], format='%Y-%m-%d')

start_date = '2023-01-01'
end_date = '2024-04-30'
df = df[(df['Data_do_pedido'] >= start_date) & (df['Data_do_pedido'] <= end_date)]

df['Pedido_Mes'] = df['Data_do_pedido'].dt.to_period('M')
df['Primeira_Compra_Mes'] = df['primeira_compra'].dt.to_period('M')

def cohort_period(df):
    df['CohortIndex'] = (df['Pedido_Mes'] - df['Primeira_Compra_Mes']).apply(lambda x: x.n)
    return df

df = df.groupby('cpf').apply(cohort_period)

cohort_data = df.pivot_table(index='Primeira_Compra_Mes', columns='CohortIndex', values='cpf', aggfunc='nunique')

cohort_data = cohort_data.fillna(0)

cohort_sizes = cohort_data.iloc[:, 0]

cohort_percentage = cohort_data.divide(cohort_sizes, axis=0)
cohort_percentage = cohort_percentage.round(2)

print(cohort_percentage)

cohort_percentage.to_csv('cohort_analysis_percentage.csv')
