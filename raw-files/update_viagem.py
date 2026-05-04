import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title
content = content.replace('<h2 class="font-display text-3xl md:text-4xl font-bold text-dark mb-2 tracking-tight">Camping & Lazer</h2>',
                          '<h2 class="font-display text-3xl md:text-4xl font-bold text-dark mb-2 tracking-tight">Viagem & Lazer</h2>')

# 2. Extract the section content and replace the products grid
start_idx = content.find('<div class="flex gap-6 md:gap-8 overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-16 pt-4" id="lancamentosCarouselContainer" style="scrollbar-width: none;">')
end_idx = content.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    # Find the closing div for the lancamentosCarouselContainer
    # We'll just find the "<!-- SECTION 7:" to know where it ends exactly and just cut out the container closing manually.
    # Actually, simpler: split by start_idx, then find the next '            </div>\n        </div>\n    </section>'
    end_div_idx = content.find('            </div>\n        </div>\n    </section>', start_idx)
    
    if end_div_idx != -1:
        # Rebuild the carousel container
        products = [
            {"name": "Mochila de Viagem 30-40L", "price": "R$ 189,90", "folder": "img/produtos/Bolsa Viagem"},
            {"name": "Travesseiro de Pescoço para Viagem", "price": "R$ 49,90", "folder": "img/produtos/Travesseiro Pescoço"},
            {"name": "Cadeira Camping Dobrável", "price": "R$ 94,90", "folder": "img/produtos/Cadeira Camping"},
            {"name": "Banquinho Dobrável Portátil", "price": "R$ 39,90", "folder": "img/produtos/Banquinho Dobrável"}
        ]
        
        new_carousel = '<div class="flex gap-6 md:gap-8 overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-16 pt-4" id="lancamentosCarouselContainer" style="scrollbar-width: none;">\n'
        
        amazon_link = "https://www.amazon.com.br/s?me=A2FL1W3S46MFWA&marketplaceID=A2Q3Y263D00KWC"
        
        for p in products:
            card = f"""                <a href="{amazon_link}" target="_blank" rel="noopener noreferrer" class="min-w-[280px] md:min-w-[320px] w-[280px] md:w-[320px] group cursor-hover snap-start flashlight-card-light relative border border-dark/5 hover:border-dark/10 bg-white transition-all duration-500 overflow-hidden block" onmousemove="const rect = this.getBoundingClientRect(); this.style.setProperty('--mouse-x', `${{event.clientX - rect.left}}px`); this.style.setProperty('--mouse-y', `${{event.clientY - rect.top}}px`);">
                    <div class="w-full aspect-[4/5] bg-[#F9F9F9] relative overflow-hidden flex items-center justify-center p-6 border-b border-dark/5">
                        <img src="{p['folder']}/1.png" class="main-img w-full h-full object-contain mix-blend-multiply group-hover:scale-105 transition-transform duration-700" alt="{p['name']}" onerror="this.style.display='none'; this.parentElement.classList.add('bg-gray-100');">
                    </div>
                    <div class="px-6 py-6 bg-white flex flex-col h-[180px]">
                        <h3 class="font-body text-base text-dark font-medium leading-tight mb-2 group-hover:text-accent transition-colors line-clamp-2">{p['name']}</h3>
                        
                        <div class="flex items-center gap-1 text-dark/40 mb-3">
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                        </div>

                        <div class="flex justify-between items-end mt-auto">
                            <div class="flex flex-col">
                                <span class="font-display font-bold text-lg text-dark">{p['price']}</span>
                            </div>
                            <button class="w-10 h-10 rounded-full bg-dark text-white flex items-center justify-center hover:bg-accent transition-colors group-hover:scale-110">
                                <i data-lucide="shopping-cart" class="w-4 h-4"></i>
                            </button>
                        </div>
                    </div>
                </a>
"""
            new_carousel += card
        
        # Replace
        content = content[:start_idx] + new_carousel + content[end_div_idx:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated Viagem & Lazer section successfully.")
else:
    print("Could not find section.")
