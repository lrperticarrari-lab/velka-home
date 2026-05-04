import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the arrows for Mais Vendidos
arrows_old = '''                <div class="hidden md:flex items-center gap-4 mt-6 md:mt-0">
                    <button class="w-10 h-10 rounded-full border border-dark/20 flex items-center justify-center text-dark hover:bg-dark hover:text-stone transition-colors cursor-hover">
                        <i data-lucide="chevron-left" class="w-5 h-5"></i>
                    </button>
                    <button class="w-10 h-10 rounded-full border border-dark/20 flex items-center justify-center text-dark hover:bg-dark hover:text-stone transition-colors cursor-hover">
                        <i data-lucide="chevron-right" class="w-5 h-5"></i>
                    </button>
                </div>'''

arrows_new = '''                <div class="hidden md:flex items-center gap-4 mt-6 md:mt-0">
                    <button id="maisVendidosPrev" class="w-10 h-10 rounded-full border border-dark/20 flex items-center justify-center text-dark hover:bg-dark hover:text-stone transition-colors cursor-hover">
                        <i data-lucide="chevron-left" class="w-5 h-5"></i>
                    </button>
                    <button id="maisVendidosNext" class="w-10 h-10 rounded-full border border-dark/20 flex items-center justify-center text-dark hover:bg-dark hover:text-stone transition-colors cursor-hover">
                        <i data-lucide="chevron-right" class="w-5 h-5"></i>
                    </button>
                </div>'''

content = content.replace(arrows_old, arrows_new)

# 2. Extract the "Mais Vendidos" grid and replace it with a carousel
grid_start = content.find('<!-- Products Grid -->')
end_section = content.find('</section>', grid_start)

if grid_start != -1 and end_section != -1:
    prods = [
        {"name": "Organizador de Pia em Aço Carbono Preto", "price": "R$ 34,90", "link": "https://www.amazon.com.br/dp/B0GMYJWM3"},
        {"name": "Kit 2 Potes Herméticos 1,5L com Medidor", "price": "R$ 39,90", "link": "https://www.amazon.com.br/dp/B0GMY4QYJY"},
        {"name": "Chaleira de Vidro Borossilicato 950ml com Infusor", "price": "R$ 39,90", "link": "https://www.amazon.com.br/dp/B0GTRF5MSZ"},
        {"name": "Pote Hermético 1L de Vidro Borossilicato", "price": "R$ 27,90", "link": "https://www.amazon.com.br/dp/B0GMXNDW4C"},
        {"name": "Kit 2 Potes Herméticos 1L de Vidro e Bambu", "price": "R$ 49,90", "link": "https://www.amazon.com.br/dp/B0GMY5V7MM"},
        {"name": "Kit 4 Potes Herméticos 1,5L com Medidor", "price": "R$ 99,90", "link": "https://www.amazon.com.br/dp/B0GMY88Z2T"},
        {"name": "Organizador de Gavetas Modular Transparente (7 Peças)", "price": "R$ 39,90", "link": "https://www.amazon.com.br/dp/B0GR6GRLXV"}
    ]
    
    new_html = '<!-- Products Carousel -->\n            <div class="flex gap-6 md:gap-8 overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-12 pt-4 reveal-up" id="maisVendidosCarouselContainer" style="scrollbar-width: none;">\n'
    
    for p in prods:
        card = f"""                <a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="min-w-[280px] md:min-w-[320px] w-[280px] md:w-[320px] group cursor-hover snap-start relative border border-dark/5 hover:border-dark/10 bg-white transition-all duration-500 overflow-hidden flex flex-col rounded-[2rem] hover:-translate-y-2 hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)]">
                    
                    <!-- Inner Image Slider -->
                    <div class="w-full aspect-square bg-[#F9F9F9] relative overflow-hidden group/slider border-b border-dark/5">
                        <div class="flex w-full h-full overflow-x-auto snap-x snap-mandatory hide-scrollbar" style="scrollbar-width: none;" onscroll="
                            const index = Math.round(this.scrollLeft / this.clientWidth);
                            const dots = this.parentElement.querySelectorAll('.dot');
                            dots.forEach((d, i) => d.style.opacity = i === index ? '1' : '0.2');
                        ">
                            <div class="w-full h-full flex-shrink-0 snap-center p-6 flex items-center justify-center">
                                <img src="[Placeholder Imagem 1]" class="w-full h-full object-contain mix-blend-multiply group-hover:scale-105 transition-transform duration-700" alt="{p['name']}">
                            </div>
                            <div class="w-full h-full flex-shrink-0 snap-center p-6 flex items-center justify-center">
                                <img src="[Placeholder Imagem 2]" class="w-full h-full object-contain mix-blend-multiply" alt="{p['name']} Detalhe 1">
                            </div>
                            <div class="w-full h-full flex-shrink-0 snap-center p-6 flex items-center justify-center">
                                <img src="[Placeholder Imagem 3]" class="w-full h-full object-contain mix-blend-multiply" alt="{p['name']} Detalhe 2">
                            </div>
                        </div>
                        
                        <!-- Mini Carousel Arrows -->
                        <button class="absolute left-2 top-1/2 -translate-y-1/2 w-8 h-8 bg-white/90 backdrop-blur rounded-full flex items-center justify-center shadow opacity-0 group-hover/slider:opacity-100 transition-opacity z-20 hover:scale-110 hover:bg-white" onclick="event.preventDefault(); event.stopPropagation(); this.previousElementSibling.scrollBy({{left: -280, behavior: 'smooth'}})">
                            <i data-lucide="chevron-left" class="w-4 h-4 text-dark"></i>
                        </button>
                        <button class="absolute right-2 top-1/2 -translate-y-1/2 w-8 h-8 bg-white/90 backdrop-blur rounded-full flex items-center justify-center shadow opacity-0 group-hover/slider:opacity-100 transition-opacity z-20 hover:scale-110 hover:bg-white" onclick="event.preventDefault(); event.stopPropagation(); this.previousElementSibling.previousElementSibling.scrollBy({{left: 280, behavior: 'smooth'}})">
                            <i data-lucide="chevron-right" class="w-4 h-4 text-dark"></i>
                        </button>
                        
                        <!-- Dots -->
                        <div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-1.5 z-20 pointer-events-none">
                            <div class="dot w-1.5 h-1.5 rounded-full bg-dark transition-opacity" style="opacity: 1"></div>
                            <div class="dot w-1.5 h-1.5 rounded-full bg-dark transition-opacity" style="opacity: 0.2"></div>
                            <div class="dot w-1.5 h-1.5 rounded-full bg-dark transition-opacity" style="opacity: 0.2"></div>
                        </div>
                    </div>
                    
                    <div class="px-6 py-6 bg-white flex flex-col flex-1 h-[200px]">
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
        new_html += card
        
    new_html += '            </div>\n        </div>\n    '
    content = content[:grid_start] + new_html + content[end_section:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Mais Vendidos grid to horizontal double-carousel format.")
else:
    print("Could not find grid section.")
