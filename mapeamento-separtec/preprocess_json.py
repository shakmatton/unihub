# This program ensures .json data integrity.
# It will remove double entries and sort remaining objects.


import json

# Carregar o arquivo JSON original
with open('dados_separtec_final.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Remover duplicatas (considerando todos os campos exceto "Nº")
itens_vistos = set()
dados_filtrados = []

for item in dados:
    # Criar uma chave única com todos os campos exceto "Nº"
    chave = (
        item["AMBIENTE"],
        item["ENTIDADE/ÓRGÃO PROPONENTE"],
        item["MUNICÍPIO"],
        item["ÁREA TEMÁTICA/CONHECIMENTO"],
        item["TERMO FINAL"],
        item["ANO"]
    )
    if chave not in itens_vistos:
        itens_vistos.add(chave)
        dados_filtrados.append(item)

# Reordenar o campo "Nº" sequencialmente
for indice, item in enumerate(dados_filtrados, start=1):
    item["Nº"] = indice

# Salvar o novo arquivo JSON
with open('dados_separtec_final.json', 'w', encoding='utf-8') as f:
    json.dump(dados_filtrados, f, ensure_ascii=False, indent=4)

print("Arquivo modificado salvo com sucesso! Verifique 'arquivo_modificado.json'.")




'''
import json

# Carrega o arquivo original
with open('dados_separtec_final.json', 'r', encoding='utf-8') as f:
    objetos = json.load(f)

objetos_unicos = []
chaves_vistas = set()

# Percorre os objetos e remove duplicatas
for obj in objetos:
    # Converter o objeto para uma string (ordenando as chaves) para garantir consistência na comparação
    chave = json.dumps(obj, sort_keys=True, ensure_ascii=False)
    if chave not in chaves_vistas:
        chaves_vistas.add(chave)
        objetos_unicos.append(obj)

# Reordena o campo "Nº" para que fiquem de 1 até o total de objetos
for idx, obj in enumerate(objetos_unicos, start=1):
    obj["Nº"] = idx

# Salva a lista modificada em um novo arquivo JSON
with open('dados_separtec_final.json', 'w', encoding='utf-8') as f:
    json.dump(objetos_unicos, f, ensure_ascii=False, indent=4)

'''