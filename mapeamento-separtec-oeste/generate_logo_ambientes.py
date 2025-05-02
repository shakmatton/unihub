#!/usr/bin/env python3
# generate_logo_ambientes.py

import json
import os

# Ajuste este caminho se o seu JSON de dados estiver em outro local
INPUT_FILE = 'dados_separtec_final.json'
OUTPUT_FILE = 'logo_ambientes.json'

# Lista dos 57 municípios da região Oeste (conforme seu código)
municipios_oeste = [
    "ANAHY","ASSIS CHATEAUBRIAND","BOA VISTA DA APARECIDA","BRAGANEY",
    "BRASILÂNDIA DO SUL","CAFELÂNDIA","CAPITÃO LEÔNIDAS MARQUES","CASCAVEL",
    "CÉU AZUL","CORBÉLIA","DIAMANTE D´OESTE","ENTRE RIOS DO OESTE",
    "FORMOSA DO OESTE","FOZ DO IGUAÇU","FRANCISCO ALVES","GUAÍRA",
    "IGUATU","IRACEMA DO OESTE","ITAIPULÂNDIA","JESUÍTAS",
    "LINDOESTE","MARECHAL CÂNDIDO RONDON","MARIPÁ","MATELÂNDIA",
    "MEDIANEIRA","MERCEDES","MISSAL","NOVA AURORA",
    "NOVA SANTA ROSA","OURO VERDE DO OESTE","PALOTINA","PATO BRAGADO",
    "QUATRO PONTES","RAMILÂNDIA","SANTA HELENA","SANTA LÚCIA",
    "SANTA TEREZA DO OESTE","SANTA TEREZINHA DE ITAIPU",
    "SÃO JOSÉ DAS PALMEIRAS","SÃO MIGUEL DO IGUAÇU",
    "SÃO PEDRO DO IGUAÇU","SERRANÓPOLIS DO IGUAÇU",
    "TERRA ROXA","TOLEDO","TUPÃSSI","UBIRATÃ","VERA CRUZ DO OESTE"
]

def main():
    if not os.path.isfile(INPUT_FILE):
        print(f"Arquivo de entrada não encontrado: {INPUT_FILE}")
        return

    # Carrega os dados originais
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    seen = set()
    logo_entries = []

    # Para cada item, se for município do oeste, adiciona uma entrada única
    for item in data:
        mun = item['MUNICÍPIO'].upper().strip()
        area = item['ÁREA TEMÁTICA/CONHECIMENTO'].strip()
        amb = item['AMBIENTE'].strip()
        if mun in municipios_oeste:
            key = (amb, mun, area)
            if key not in seen:
                seen.add(key)
                logo_entries.append({
                    "AMBIENTE": amb,
                    "MUNICÍPIO": mun,
                    "ÁREA TEMÁTICA/CONHECIMENTO": area,
                    "LINK_LOGO": ""  # aqui você preencherá depois os caminhos dos arquivos
                })

    # Grava o JSON final
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(logo_entries, f, ensure_ascii=False, indent=2)

    print(f"Gerado {len(logo_entries)} entradas em {OUTPUT_FILE}")

if __name__ == '__main__':
    main()

