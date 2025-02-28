import json
import re

# Carregar o arquivo JSON original
with open('dados_separtec_final.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Padronizar "ENTIDADE/ÓRGÃO PROPONENTE"
for item in dados:
    entidade = item["ENTIDADE/ÓRGÃO PROPONENTE"].strip()  # Remove espaços extras
    # Verifica se começa com "PREFEITURA MUNICIPAL DE" (case insensitive)
    if re.match(r'^PREFEITURA MUNICIPAL DE\b', entidade, re.IGNORECASE):
        item["ENTIDADE/ÓRGÃO PROPONENTE"] = "PREFEITURA MUNICIPAL"

# Salvar o novo arquivo JSON
with open('dados_separtec_final.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("Arquivo modificado salvo com sucesso!")