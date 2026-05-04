import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Potes Herméticos -> Potes herméticos
content = re.sub(r'<span class="font-body text-sm text-dark font-medium tracking-wide">Potes Herméticos</span>', 
                 '<span class="font-body text-sm text-dark font-medium tracking-wide">Potes herméticos</span>', content)

# 2. Soluções para o banheiro
content = re.sub(r'<img src="[^"]*" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Soluções para o banheiro">',
                 '<img src="https://images.unsplash.com/photo-1620626011761-996317b8d101?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Soluções para o banheiro">', content)

# 3. Caixas e Cestos
content = re.sub(r'<img src="[^"]*" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Caixas e Cestos">',
                 '<img src="https://images.unsplash.com/photo-1616401784845-180882ba9ba8?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Caixas e Cestos">', content)

# 4. Servir & Decorar
content = re.sub(r'<img src="[^"]*" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Servir & Decorar">',
                 '<img src="https://images.unsplash.com/photo-1615876234886-fd9a39fda97f?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Servir & Decorar">', content)

# 5. Viagem e lazer
content = re.sub(r'<img src="[^"]*" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Viagem e Lazer">',
                 '<img src="https://images.unsplash.com/photo-1504280390224-340cb253e670?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Viagem e lazer">', content)
content = re.sub(r'<span class="font-body text-sm text-dark font-medium tracking-wide">Viagem & Lazer</span>', 
                 '<span class="font-body text-sm text-dark font-medium tracking-wide">Viagem e lazer</span>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
