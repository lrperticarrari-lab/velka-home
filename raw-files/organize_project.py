import os
import shutil
import re

# 1. Create Directories
dirs = ['css', 'js', 'img/categorias', 'img/produtos', 'raw-files']
for d in dirs:
    os.makedirs(d, exist_ok=True)

# 2. Move category images
if os.path.exists('fotos-categorias-site'):
    for f in os.listdir('fotos-categorias-site'):
        shutil.move(os.path.join('fotos-categorias-site', f), os.path.join('img/categorias', f))
    os.rmdir('fotos-categorias-site')

# 3. Move product images
if os.path.exists('Banco de Imagens'):
    for f in os.listdir('Banco de Imagens'):
        shutil.move(os.path.join('Banco de Imagens', f), os.path.join('img/produtos', f))
    os.rmdir('Banco de Imagens')

# 4. Move raw files
raw_files = [f for f in os.listdir('.') if f.endswith('.py') and f != 'organize_project.py']
raw_files += [f for f in os.listdir('.') if f.endswith('.xlsx') or f.endswith('.json') or f.endswith('.zip')]
raw_dirs = ['fotos-dos-produtos', '_referencias', 'assets']
for f in raw_files:
    if os.path.exists(f):
        shutil.move(f, os.path.join('raw-files', f))
for d in raw_dirs:
    if os.path.exists(d):
        shutil.move(d, os.path.join('raw-files', d))

# 5. Move any loose js
if os.path.exists('scripts.js'):
    shutil.move('scripts.js', 'js/scripts.js')

# 6. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace image paths
content = content.replace('fotos-categorias-site/', 'img/categorias/')
content = content.replace('Banco de Imagens/', 'img/produtos/')

# Extract CSS
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    content = content.replace(style_match.group(0), '<link rel="stylesheet" href="css/style.css">')

# Extract custom JS (everything inside the last script tags)
# There are multiple script tags at the end. Let's find all script tags that don't have src.
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
js_content = ""
for script in scripts:
    # Skip tailwind config
    if 'tailwind.config' in script:
        continue
    js_content += script.strip() + "\n\n"

if js_content:
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    # Remove all extracted inline scripts and add the external link
    for script in scripts:
        if 'tailwind.config' not in script:
            content = content.replace(f'<script>{script}</script>', '')
    
    # Add the link before </body>
    content = content.replace('</body>', '    <script src="js/main.js"></script>\n</body>')
    # Clean up empty lines from removed scripts
    content = re.sub(r'(\s*<!--.*?-->\s*)*\n\s*\n\s*<script src="js/main.js"></script>', '\n    <script src="js/main.js"></script>', content)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Project organized successfully!")
