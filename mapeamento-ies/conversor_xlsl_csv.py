import pandas as pd

# Ler o arquivo Excel
data = pd.read_excel('Dados_IES_small.xlsx')

# Converter para CSV
data.to_csv('Dados_IES_small.csv', index=False)
