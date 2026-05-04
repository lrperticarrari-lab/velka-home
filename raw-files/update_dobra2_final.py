import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s2_start = content.find("<!-- Categories Grid/Carousel -->")
s3_start = content.find("<!-- SECTION 3: MAIS VENDIDOS -->")

if s2_start != -1 and s3_start != -1:
    
    cats = [
        {"name": "Cozinha e Servir", "img": "fotos-categorias-site/potes-hermeticos.png"},
        {"name": "Organização Inteligente", "img": "fotos-categorias-site/gaveta-quarto.png"},
        {"name": "Essenciais de Casa", "img": "fotos-categorias-site/Cesto-roupa.png"},
        {"name": "Viagem e Lazer", "img": "fotos-categorias-site/camping-lazer.png"}
    ]
    
    new_html = '<!-- Categories Grid/Carousel -->\n            <div class="flex overflow-x-auto gap-6 md:gap-8 pb-12 snap-x hide-scrollbar px-4 md:px-0" style="scrollbar-width: none;">\n'
    
    for i, cat in enumerate(cats):
        delay = i * 0.15
        
        card_html = f"""
                <!-- Cat {i+1} -->
                <a href="https://www.amazon.com.br" target="_blank" rel="noopener noreferrer" class="min-w-[280px] w-[280px] md:min-w-[0] md:flex-1 group cursor-hover snap-center relative p-[1px] rounded-[1.25rem] transition-all duration-700 hover:-translate-y-3 hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.1)] reveal-up" style="transition-delay: {delay}s;">
                    
                    <!-- Spinning Border Beam (Visible on Hover) -->
                    <span class="absolute inset-[-100%] animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,transparent_75%,rgba(0,0,0,0.25)_100%)] opacity-0 transition-opacity duration-500 group-hover:opacity-100 rounded-full"></span>
                    
                    <!-- Card Background and Flashlight Effect -->
                    <div class="relative w-full h-full flex flex-col bg-white z-10 flashlight-card-light overflow-hidden rounded-[1.25rem] ring-1 ring-black/5" onmousemove="const rect = this.getBoundingClientRect(); this.style.setProperty('--mouse-x', `${{event.clientX - rect.left}}px`); this.style.setProperty('--mouse-y', `${{event.clientY - rect.top}}px`);">
                        
                        <!-- Internal Gradient / Subtle Background Texture -->
                        <div class="absolute inset-0 bg-gradient-to-br from-stone-50 to-stone-100 opacity-50 pointer-events-none"></div>

                        <div class="w-full aspect-[4/5] overflow-hidden relative flex items-center justify-center">
                            
                            <!-- Premium Image Animation: zoom on hover, subtle floating -->
                            <img src="{cat['img']}" class="w-full h-full object-cover group-hover:scale-105 group-hover:-translate-y-2 transition-transform duration-[800ms] ease-[cubic-bezier(0.25,1,0.5,1)] relative z-10" alt="{cat['name']}">
                            
                            <!-- Glass Panel Label (Premium UI - Centered Bottom) -->
                            <div class="absolute bottom-4 left-1/2 -translate-x-1/2 w-[calc(100%-2rem)] bg-white/80 backdrop-blur-xl border border-white/60 py-4 px-4 text-center transform translate-y-4 opacity-90 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-[600ms] ease-[cubic-bezier(0.16,1,0.3,1)] shadow-[0_8px_30px_rgb(0,0,0,0.06)] rounded-xl z-20 flex flex-col items-center justify-center">
                                <span class="font-body text-xs md:text-sm text-dark font-semibold tracking-wider uppercase z-10">{cat['name']}</span>
                            </div>
                        </div>
                    </div>
                </a>
"""
        new_html += card_html
        
    new_html += '            </div>\n        </div>\n    </section>\n\n    '
    
    content = content[:s2_start] + new_html + content[s3_start:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Dobra 2 replaced with local images and 4 cards.")
else:
    print("Markers not found.")
