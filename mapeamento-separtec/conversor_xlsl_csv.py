import pandas as pd

# Ler o arquivo Excel
data = pd.read_excel('dados_separtec_final.xlsx')

# Converter para CSV
data.to_csv('dados_separtec_final.csv', index=False, encoding='utf-8') # Certificar-se da codificação utf-8
