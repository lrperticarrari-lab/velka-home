import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s2_start = content.find("<!-- SECTION 2: CATEGORIAS -->")
s3_start = content.find("<!-- SECTION 3: MAIS VENDIDOS -->")

if s2_start != -1 and s3_start != -1:
    s2_content = content[s2_start:s3_start]
    
    replacements = {
        # 1. Potes herméticos
        "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?q=80&w=800&auto=format&fit=crop": "https://images.unsplash.com/photo-1556910103-1c02745aae4d?q=80&w=800&auto=format&fit=crop",
        
        # 2. Banheiro
        "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=800&auto=format&fit=crop": "https://images.unsplash.com/photo-1585421514738-01798e348b17?q=80&w=800&auto=format&fit=crop",
        
        # 3. Caixas e Cestos
        "https://images.unsplash.com/photo-1595526114101-11b0e501a3cd?q=80&w=800&auto=format&fit=crop": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?q=80&w=800&auto=format&fit=crop",
        
        # 4. Servir & Decorar
        "https://images.unsplash.com/photo-1577140917170-285929fb55b7?q=80&w=800&auto=format&fit=crop": "https://images.unsplash.com/photo-1615873968403-89e068629265?q=80&w=800&auto=format&fit=crop",
        
        # 5. Viagem e Lazer
        "https://images.unsplash.com/photo-1553901753-215db0446d9a?q=80&w=800&auto=format&fit=crop": "https://images.unsplash.com/photo-1569949381669-ecf31ae8e613?q=80&w=800&auto=format&fit=crop"
    }
    
    for old, new in replacements.items():
        s2_content = s2_content.replace(old, new)
        
    content = content[:s2_start] + s2_content + content[s3_start:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Images updated in Dobra 2!")
