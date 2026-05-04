import os
import shutil

base_dir = '/Users/leonardoperticarrari/Desktop/curso-design/Construindo site estáticos com IA/SITE-VELKA-HOME/img/produtos/'

# Folders to rename:
renames = [
    ('Potes Herméticos Tampa Bambu', 'potes-hermeticos-tampa-bambu'),
    ('Dispenser Alimentos e Sabão', 'dispenser-alimentos-e-sabao'),
    ('Travesseiro Pescoço', 'travesseiro-pescoco'),
    ('Banquinho Dobrável', 'banquinho-dobravel')
]

for old, new in renames:
    old_path = os.path.join(base_dir, old)
    new_path = os.path.join(base_dir, new)
    
    # Try different normalizations if direct match fails due to macOS NFD
    if not os.path.exists(old_path):
        import unicodedata
        for f in os.listdir(base_dir):
            if unicodedata.normalize('NFC', f) == unicodedata.normalize('NFC', old):
                old_path = os.path.join(base_dir, f)
                break
                
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")
    else:
        print(f"Could not find: {old_path}")

# Update index.html
with open('/Users/leonardoperticarrari/Desktop/curso-design/Construindo site estáticos com IA/SITE-VELKA-HOME/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace strings in content
# Since macOS might use decomposed characters in the HTML too, we should just search both or exact strings in HTML
import unicodedata

# Let's just do direct replacements
replacements = {
    'Potes Herméticos Tampa Bambu': 'potes-hermeticos-tampa-bambu',
    'Dispenser Alimentos e Sabão': 'dispenser-alimentos-e-sabao',
    'Travesseiro Pescoço': 'travesseiro-pescoco',
    'Banquinho Dobrável': 'banquinho-dobravel'
}

for old, new in replacements.items():
    content = content.replace(old, new)
    content = content.replace(unicodedata.normalize('NFC', old), new)
    content = content.replace(unicodedata.normalize('NFD', old), new)

with open('/Users/leonardoperticarrari/Desktop/curso-design/Construindo site estáticos com IA/SITE-VELKA-HOME/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
