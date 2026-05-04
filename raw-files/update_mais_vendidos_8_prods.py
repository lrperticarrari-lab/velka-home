import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate SECTION 3: MAIS VENDIDOS
start_idx = content.find('<!-- SECTION 3: MAIS VENDIDOS -->')
end_idx = content.find('<!-- SECTION 4: CARROSSEL DIA DAS MÃES', start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find bounds of Mais Vendidos")
    exit(1)

section_content = content[start_idx:end_idx]

carousel_start = section_content.find('<!-- Products Carousel -->')
carousel_end = section_content.find('</section>')

prods = [
    {
        "name": "Organizador de Pia em Aço Carbono Preto",
        "price": "R$ 34,90",
        "link": "https://www.amazon.com.br/dp/B0GMYJWM3",
        "imgs": ["img/produtos/Suporte Pia/1.png", "img/produtos/Suporte Pia/2.png", "img/produtos/Suporte Pia/3.png"]
    },
    {
        "name": "Chaleira de Vidro Borossilicato 950ml com Infusor",
        "price": "R$ 39,90",
        "link": "https://www.amazon.com.br/dp/B0GTRF5MSZ",
        "imgs": ["img/produtos/Chaleira Infusor/1.png", "img/produtos/Chaleira Infusor/2.png", "img/produtos/Chaleira Infusor/3.png"]
    },
    {
        "name": "Pote Hermético 1L de Vidro Borossilicato",
        "price": "R$ 27,90",
        "link": "https://www.amazon.com.br/dp/B0GMXNDW4C",
        "imgs": ["img/produtos/Potes Herméticos Tampa Bambu/1.png", "img/produtos/Potes Herméticos Tampa Bambu/2.png", "img/produtos/Potes Herméticos Tampa Bambu/3.png"]
    },
    {
        "name": "Kit 2 Potes Herméticos 1,5L com Medidor",
        "price": "R$ 39,90",
        "link": "https://www.amazon.com.br/dp/B0GMY4QYJY",
        "imgs": ["img/produtos/Dispenser Alimentos e Sabão/1.png", "img/produtos/Dispenser Alimentos e Sabão/2.png", "img/produtos/Dispenser Alimentos e Sabão/1.png"]
    },
    {
        "name": "Petisqueira Bambu 25cm 5 Divisórias",
        "price": "R$ 64,90",
        "link": "https://www.amazon.com.br/dp/B0GT76NBV8",
        "imgs": ["img/produtos/Petisqueira/1.png", "img/produtos/Petisqueira/2.png", "img/produtos/Petisqueira/3.png"]
    },
    {
        "name": "Escorredor Porta Talheres Inox",
        "price": "R$ 34,90",
        "link": "https://www.amazon.com.br/dp/B0GMYDZTTD",
        "imgs": ["img/produtos/Escorredor Talheres/1.png", "img/produtos/Escorredor Talheres/2.png", "img/produtos/Escorredor Talheres/3.png"]
    },
    {
        "name": "Organizador de Gavetas Modular Transparente",
        "price": "R$ 39,90",
        "link": "https://www.amazon.com.br/dp/B0GR6GRLXV",
        "imgs": ["img/produtos/Kit organizadores gaveta/1.png", "img/produtos/Kit organizadores gaveta/2.png", "img/produtos/Kit organizadores gaveta/3.png"]
    },
    {
        "name": "Porta Ovos 32un Gavetas Deslizantes",
        "price": "R$ 49,90",
        "link": "https://www.amazon.com.br/dp/B0GPF7FFXF",
        "imgs": ["img/produtos/Organizador de ovos/1.png", "img/produtos/Organizador de ovos/2.png", "img/produtos/Organizador de ovos/3.png"]
    }
]

new_carousel = '<!-- Products Carousel -->\n            <div class="flex gap-6 md:gap-8 overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-12 pt-4 reveal-up" id="maisVendidosCarouselContainer" style="scrollbar-width: none;">\n'

for p in prods:
    card = f"""                <a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="min-w-[280px] md:min-w-[320px] w-[280px] md:w-[320px] group cursor-hover snap-start relative border border-dark/5 bg-white transition-all duration-500 overflow-hidden flex flex-col rounded-[2rem] hover:-translate-y-2 hover:shadow-[0_30px_60px_-15px_rgba(0,0,0,0.12)] flashlight-card-light" onmousemove="const rect = this.getBoundingClientRect(); this.style.setProperty('--mouse-x', `${{event.clientX - rect.left}}px`); this.style.setProperty('--mouse-y', `${{event.clientY - rect.top}}px`);">
                    <!-- Premium Shimmer -->
                    <div class="absolute inset-0 -translate-x-full bg-gradient-to-r from-transparent via-white/50 to-transparent group-hover:animate-[shimmer-light_1.5s_infinite] pointer-events-none z-30 rounded-[2rem] overflow-hidden"></div>
                    
                    <!-- Inner Image Slider -->
                    <div class="w-full aspect-square bg-[#F9F9F9] relative overflow-hidden group/slider border-b border-dark/5">
                        <div class="flex w-full h-full overflow-x-auto snap-x snap-mandatory hide-scrollbar" style="scrollbar-width: none;" onscroll="
                            const index = Math.round(this.scrollLeft / this.clientWidth);
                            const dots = this.parentElement.querySelectorAll('.dot');
                            dots.forEach((d, i) => d.style.opacity = i === index ? '1' : '0.2');
                        ">
                            <div class="w-full h-full flex-shrink-0 snap-center p-6 flex items-center justify-center">
                                <img src="{p['imgs'][0]}" class="w-full h-full object-contain mix-blend-multiply group-hover:scale-105 transition-transform duration-700" alt="{p['name']}">
                            </div>
                            <div class="w-full h-full flex-shrink-0 snap-center p-6 flex items-center justify-center">
                                <img src="{p['imgs'][1]}" class="w-full h-full object-contain mix-blend-multiply" alt="{p['name']} Detalhe 1" onerror="this.src='{p['imgs'][0]}'">
                            </div>
                            <div class="w-full h-full flex-shrink-0 snap-center p-6 flex items-center justify-center">
                                <img src="{p['imgs'][2]}" class="w-full h-full object-contain mix-blend-multiply" alt="{p['name']} Detalhe 2" onerror="this.src='{p['imgs'][0]}'">
                            </div>
                        </div>
                        
                        <!-- Mini Carousel Arrows -->
                        <button class="absolute left-2 top-1/2 -translate-y-1/2 w-8 h-8 bg-white/90 backdrop-blur rounded-full flex items-center justify-center shadow opacity-0 group-hover/slider:opacity-100 transition-opacity z-40 hover:scale-110 hover:bg-white" onclick="event.preventDefault(); event.stopPropagation(); this.previousElementSibling.scrollBy({{left: -280, behavior: 'smooth'}})">
                            <i data-lucide="chevron-left" class="w-4 h-4 text-dark"></i>
                        </button>
                        <button class="absolute right-2 top-1/2 -translate-y-1/2 w-8 h-8 bg-white/90 backdrop-blur rounded-full flex items-center justify-center shadow opacity-0 group-hover/slider:opacity-100 transition-opacity z-40 hover:scale-110 hover:bg-white" onclick="event.preventDefault(); event.stopPropagation(); this.previousElementSibling.previousElementSibling.scrollBy({{left: 280, behavior: 'smooth'}})">
                            <i data-lucide="chevron-right" class="w-4 h-4 text-dark"></i>
                        </button>
                        
                        <!-- Dots -->
                        <div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-1.5 z-40 pointer-events-none">
                            <div class="dot w-1.5 h-1.5 rounded-full bg-dark transition-opacity" style="opacity: 1"></div>
                            <div class="dot w-1.5 h-1.5 rounded-full bg-dark transition-opacity" style="opacity: 0.2"></div>
                            <div class="dot w-1.5 h-1.5 rounded-full bg-dark transition-opacity" style="opacity: 0.2"></div>
                        </div>
                    </div>
                    
                    <div class="px-6 py-6 bg-white flex flex-col flex-1 h-[200px] z-10">
                        <h3 class="font-body text-base text-dark font-medium leading-tight mb-2 group-hover:text-accent transition-colors line-clamp-2">{p['name']}</h3>
                        
                        <div class="flex items-center gap-1 text-dark/40 mb-auto">
                            <i data-lucide="star" class="w-3.5 h-3.5 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3.5 h-3.5 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3.5 h-3.5 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3.5 h-3.5 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3.5 h-3.5 fill-current text-dark/80"></i>
                        </div>

                        <div class="flex justify-between items-end mt-4">
                            <div class="flex flex-col">
                                <span class="font-display font-bold text-xl text-dark">{p['price']}</span>
                            </div>
                            <div class="w-10 h-10 rounded-full bg-dark text-white flex items-center justify-center hover:bg-accent transition-colors group-hover:scale-110 group-hover:shadow-lg">
                                <i data-lucide="shopping-cart" class="w-4 h-4"></i>
                            </div>
                        </div>
                    </div>
                </a>
"""
    new_carousel += card

new_carousel += '            </div>\n        </div>\n    '

new_section_content = section_content[:carousel_start] + new_carousel

new_content = content[:start_idx] + new_section_content + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Mais Vendidos carousel to 8 products!")
