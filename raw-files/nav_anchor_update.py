import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Desktop Nav
desktop_nav_old = """            <!-- Center: Links (Desktop) -->
            <div class="hidden md:flex items-center gap-10 font-body text-sm font-medium">
                <a href="#" class="nav-link text-white/90 hover:text-white">Início</a>
                <a href="#" class="nav-link text-white/90 hover:text-white">Cozinha</a>
                <a href="#" class="nav-link text-white/90 hover:text-white">Organização</a>
                <a href="#" class="nav-link text-white/90 hover:text-white">Iluminação</a>
                <a href="#" class="nav-link text-white/90 hover:text-white">Contato</a>
            </div>"""

desktop_nav_new = """            <!-- Center: Links (Desktop) -->
            <div class="hidden md:flex items-center gap-10 font-body text-sm font-medium">
                <a href="#inicio" class="nav-link text-white/90 hover:text-white transition-colors">Início</a>
                <a href="#mais-vendidos" class="nav-link text-white/90 hover:text-white transition-colors">Mais Vendidos</a>
                <a href="#casa-organizacao" class="nav-link text-white/90 hover:text-white transition-colors">Casa & Organização</a>
                <a href="#viagem-lazer" class="nav-link text-white/90 hover:text-white transition-colors">Viagem & Lazer</a>
                <a href="#contato" class="nav-link text-white/90 hover:text-white transition-colors">Contato</a>
            </div>"""

content = content.replace(desktop_nav_old, desktop_nav_new)


# 2. Update Mobile Nav
mobile_nav_old = """        <div class="flex flex-col gap-8 font-display text-3xl sm:text-4xl font-bold tracking-tight text-white/90">
            <a href="#" class="mobile-link hover:text-white transition-colors">Início</a>
            <a href="#" class="mobile-link hover:text-white transition-colors">Cozinha</a>
            <a href="#" class="mobile-link hover:text-white transition-colors">Organização</a>
            <a href="#" class="mobile-link hover:text-white transition-colors">Iluminação</a>
            <a href="#" class="mobile-link hover:text-white transition-colors">Contato</a>
        </div>"""

mobile_nav_new = """        <div class="flex flex-col gap-8 font-display text-3xl sm:text-4xl font-bold tracking-tight text-white/90">
            <a href="#inicio" class="mobile-link hover:text-white transition-colors">Início</a>
            <a href="#mais-vendidos" class="mobile-link hover:text-white transition-colors">Mais Vendidos</a>
            <a href="#casa-organizacao" class="mobile-link hover:text-white transition-colors">Casa & Organização</a>
            <a href="#viagem-lazer" class="mobile-link hover:text-white transition-colors">Viagem & Lazer</a>
            <a href="#contato" class="mobile-link hover:text-white transition-colors">Contato</a>
        </div>"""

content = content.replace(mobile_nav_old, mobile_nav_new)


# 3. Add IDs to sections
# Hero
content = content.replace(
    '<section class="relative h-[100svh] w-full flex flex-col justify-center overflow-hidden bg-[#0A0A0A]">',
    '<section id="inicio" class="relative h-[100svh] w-full flex flex-col justify-center overflow-hidden bg-[#0A0A0A]">'
)

# Casa e Organizacao
content = content.replace(
    '<section class="py-16 md:py-24 px-6 md:px-12 lg:px-20 bg-stone w-full reveal-up">',
    '<section id="casa-organizacao" class="py-16 md:py-24 px-6 md:px-12 lg:px-20 bg-stone w-full reveal-up">'
)

# Viagem & Lazer
content = content.replace(
    '<section class="py-20 md:py-32 px-6 md:px-12 lg:px-20 bg-white w-full border-t border-dark/5 relative overflow-hidden">',
    '<section id="viagem-lazer" class="py-20 md:py-32 px-6 md:px-12 lg:px-20 bg-white w-full border-t border-dark/5 relative overflow-hidden">'
)

# Contato
content = content.replace(
    '<footer class="w-full bg-[#0A0A0A] text-white pt-20 pb-24 md:pb-8 px-6 md:px-12 lg:px-20 border-t border-white/10 relative z-10">',
    '<footer id="contato" class="w-full bg-[#0A0A0A] text-white pt-20 pb-24 md:pb-8 px-6 md:px-12 lg:px-20 border-t border-white/10 relative z-10">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML anchors updated.")
