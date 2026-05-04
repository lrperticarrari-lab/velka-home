import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the labels and make sure the images match the context
# The images are currently:
# 1. photo-1670426502388-8bbf710a63f2 (potes)
# 2. photo-1584622650111-993a426fbf0a (banheiro - wait, earlier it was 'Soluções para a pia')
# 3. photo-1595988276927-5a1fadc561b4 (caixas)
# 4. photo-1447949122973-9711a09951d5 (servir)
# 5. photo-1499803270242-467f7311582d (viagem)

content = content.replace('alt="Soluções para a pia"', 'alt="Soluções para o banheiro"')
content = content.replace('<span class="font-body text-sm text-dark font-medium tracking-wide">Soluções para a pia</span>', '<span class="font-body text-sm text-dark font-medium tracking-wide">Soluções para o banheiro</span>')

# Let's ensure the image for "Potes Herméticos" is good. The current one is fine.
# We will just verify all labels match exactly.
# 1. Potes Herméticos
content = content.replace('alt="Potes Herméticos"', 'alt="Potes Herméticos"')
# 2. Soluções para o banheiro
# 3. Caixas e Cestos
content = content.replace('alt="Caixas e Cestos"', 'alt="Caixas e Cestos"')
# 4. Servir & Decorar
content = content.replace('alt="Mesa Posta e Servir"', 'alt="Servir & Decorar"')
content = content.replace('<span class="font-body text-sm text-dark font-medium tracking-wide">Mesa Posta e Servir</span>', '<span class="font-body text-sm text-dark font-medium tracking-wide">Servir & Decorar</span>')

# 5. Viagem & Lazer
content = content.replace('alt="Viagem e Lazer"', 'alt="Viagem e Lazer"')
content = content.replace('<span class="font-body text-sm text-dark font-medium tracking-wide">Viagem e Lazer</span>', '<span class="font-body text-sm text-dark font-medium tracking-wide">Viagem e Lazer</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
