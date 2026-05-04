import pandas as pd
import os
import json

df = pd.read_excel('VORA_Produtos.xlsx')
products = []
for index, row in df.iterrows():
    preco = str(row.get('Preço', '—')).strip()
    if preco == '—' or preco == 'nan':
        continue
    
    pasta_drive = str(row.get('Pasta no Drive', '')).strip()
    nome_curto = str(row.get('Nome Curto (Site)', '')).strip()
    categoria = str(row.get('Categoria', '')).strip()
    
    pasta_path = os.path.join('Banco de Imagens', pasta_drive)
    imagens = []
    if os.path.isdir(pasta_path):
        # get all files
        for f in os.listdir(pasta_path):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                imagens.append(os.path.join('Banco de Imagens', pasta_drive, f))
        imagens.sort() # sort alphabetically to get consistent ordering
        
    products.append({
        'nome': nome_curto,
        'preco': preco,
        'categoria': categoria,
        'pasta': pasta_drive,
        'imagens': imagens
    })

print(json.dumps(products, indent=2, ensure_ascii=False))
