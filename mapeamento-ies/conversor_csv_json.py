import pandas as pd
#import json

# Ler o arquivo CSV
data = pd.read_csv('Dados_IES_small.csv', encoding='utf-8') # Adicione encoding='utf-8' se tiver caracteres especiais

# Converter para JSON (lista de objetos)
json_data = data.to_json(orient='records', indent=4, force_ascii=False)

# Salvar o JSON em um arquivo
with open('dados-ies.json', 'w', encoding='utf-8') as f: # Adicione encoding='utf-8' para caracteres especiais
    f.write(json_data)

print("Arquivo JSON 'dados-ies.json' criado com sucesso.")