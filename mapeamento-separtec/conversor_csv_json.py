import pandas as pd

# Ler o arquivo CSV
data = pd.read_csv('dados_separtec_final_2.csv', encoding='utf-8')
# Cuidado: lembrar que esse arquivo é diferente do arquivo "dados_separtec_final.csv"

# Padronizar os campos em maiúsculas ou minúsculas
data['MUNICÍPIO'] = data['MUNICÍPIO'].str.upper() # ou .str.lower()

# Converter para JSON (lista de objetos)
json_data = data.to_json(orient='records', indent=4, force_ascii=False)

# Salvar o JSON em um arquivo
with open('dados_separtec_final_2.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print("Arquivo JSON 'dados_separtec_final_2.json' criado com sucesso.")
