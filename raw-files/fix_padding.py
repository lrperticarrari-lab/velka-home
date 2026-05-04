import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s2_start = content.find("<!-- SECTION 2: CATEGORIAS -->")
s3_start = content.find("<!-- SECTION 3: MAIS VENDIDOS -->")

if s2_start != -1 and s3_start != -1:
    s2_content = content[s2_start:s3_start]
    
    # Remove p-8 padding so the lifestyle images fully cover the cards
    s2_content = s2_content.replace('<div class="w-full aspect-[4/5] overflow-hidden relative flex items-center justify-center p-8">', '<div class="w-full aspect-[4/5] overflow-hidden relative flex items-center justify-center">')
    
    # Also in the style, remove the inner bg-white/50 if present. In the previous turn, it was replaced by gradient but let's check.
    # From line 389: <div class="absolute inset-0 bg-gradient-to-br from-stone-50 to-stone-100 opacity-50 pointer-events-none"></div>
    # Actually, if the image covers the whole card and is z-10, the background doesn't matter much.
    
    content = content[:s2_start] + s2_content + content[s3_start:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed p-8 padding in Dobra 2")
