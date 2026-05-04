import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Top Bar
content = content.replace(
    '<div class="bg-accent text-stone text-[10px] md:text-xs font-mono uppercase tracking-widest py-2 text-center w-full">',
    '<div class="bg-accent text-stone text-[9px] sm:text-[10px] md:text-xs font-mono uppercase tracking-widest py-2.5 px-4 leading-tight text-center w-full">'
)

# 2. Update Mobile Menu Toggle Button
content = content.replace(
    '''            <!-- Mobile Menu Toggle -->
            <button class="md:hidden text-white" aria-label="Menu">
                <i data-lucide="menu" class="w-6 h-6"></i>
            </button>''',
    '''            <!-- Mobile Menu Toggle -->
            <button id="mobileMenuBtn" class="md:hidden text-white z-[60] relative p-2 -mr-2" aria-label="Menu">
                <i data-lucide="menu" class="w-6 h-6"></i>
            </button>'''
)

# 3. Add Mobile Menu Overlay after Header
mobile_menu_html = '''
    <!-- Mobile Menu Overlay -->
    <div id="mobileMenu" class="fixed inset-0 bg-[#0A0A0A] z-[55] translate-x-full transition-transform duration-500 ease-[cubic-bezier(0.33,1,0.68,1)] flex flex-col pt-28 px-6 pb-12 md:hidden">
        <div class="flex flex-col gap-8 font-display text-3xl sm:text-4xl font-bold tracking-tight text-white/90">
            <a href="#" class="mobile-link hover:text-white transition-colors">Início</a>
            <a href="#" class="mobile-link hover:text-white transition-colors">Cozinha</a>
            <a href="#" class="mobile-link hover:text-white transition-colors">Organização</a>
            <a href="#" class="mobile-link hover:text-white transition-colors">Iluminação</a>
            <a href="#" class="mobile-link hover:text-white transition-colors">Contato</a>
        </div>
        <div class="mt-auto flex flex-col gap-4">
            <a href="https://www.amazon.com.br/s?me=A2FL1W3S46MFWA&marketplaceID=A2Q3Y263D00KWC" target="_blank" rel="noopener noreferrer" class="font-mono text-xs uppercase tracking-widest border border-white/20 rounded-full px-5 py-4 text-center text-white hover:bg-white hover:text-dark transition-all duration-300 w-full min-h-[48px] flex items-center justify-center">
                Nossa Loja na Amazon
            </a>
        </div>
    </div>
'''
content = content.replace('    </header>', '    </header>\n' + mobile_menu_html)

# 4. Hero Content adjustments
content = content.replace(
    '<div class="w-full lg:w-[60%] flex flex-col items-start text-left">',
    '<div class="w-full lg:w-[60%] flex flex-col items-start text-left mt-16 md:mt-0">'
)

content = content.replace(
    '<h1 class="font-display text-[2.6rem] sm:text-6xl md:text-7xl lg:text-[6.5rem] font-bold uppercase tracking-tighter mb-2 leading-[0.85] text-white">',
    '<h1 class="font-display text-[2.2rem] sm:text-5xl md:text-7xl lg:text-[6.5rem] font-bold uppercase tracking-tighter mb-2 leading-[0.9] md:leading-[0.85] text-white">'
)

content = content.replace(
    '<div class="hero-fade flex flex-col sm:flex-row gap-6 items-center justify-start w-full sm:w-auto">',
    '<div class="hero-fade flex flex-col sm:flex-row gap-4 md:gap-6 items-center justify-start w-full sm:w-auto">'
)

# Ensure Button 1 spans full width and has min-h-[48px] (it already has py-4 which is 16px*2 + text, > 48px, but let's be explicit)
content = content.replace(
    '<span class="relative flex h-full w-full items-center justify-center rounded-full bg-[#0A0A0A] backdrop-blur-xl px-8 py-4 ring-1 ring-white/[0.06]">',
    '<span class="relative flex h-full w-full items-center justify-center rounded-full bg-[#0A0A0A] backdrop-blur-xl px-8 py-4 min-h-[48px] ring-1 ring-white/[0.06]">'
)

# Same for secondary button
content = content.replace(
    '<a href="#mais-vendidos" class="group relative flex items-center justify-center gap-3 px-8 py-4 rounded-full bg-white/[0.03] border border-white/10 backdrop-blur-lg overflow-hidden transition-all duration-500 hover:scale-105 hover:bg-white/[0.08] hover:border-white/30 hover:shadow-[0_0_40px_-10px_rgba(255,255,255,0.15)] w-full sm:w-auto">',
    '<a href="#mais-vendidos" class="group relative flex items-center justify-center gap-3 px-8 py-4 min-h-[48px] rounded-full bg-white/[0.03] border border-white/10 backdrop-blur-lg overflow-hidden transition-all duration-500 hover:scale-105 hover:bg-white/[0.08] hover:border-white/30 hover:shadow-[0_0_40px_-10px_rgba(255,255,255,0.15)] w-full sm:w-auto">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("index.html updated")
