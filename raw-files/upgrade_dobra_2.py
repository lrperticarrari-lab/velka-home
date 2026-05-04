import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to isolate the categories block
start_marker = "<!-- Categories Grid/Carousel -->"
end_marker = "<!-- End Section 2 -->"

if start_marker in content and end_marker in content:
    pre = content.split(start_marker)[0]
    post = content.split(end_marker)[1]
    
    # We will rebuild the categories with premium animations
    cats = [
        {"name": "Potes herméticos", "img": "Banco de Imagens/Potes Herméticos Tampa Bambu/1.png"},
        {"name": "Soluções para o banheiro", "img": "Banco de Imagens/Suporte Toalhas/1.png"},
        {"name": "Caixas e Cestos", "img": "Banco de Imagens/Kit organizadores gaveta/1.png"},
        {"name": "Servir & Decorar", "img": "Banco de Imagens/Bandeja decorativa/1.png"},
        {"name": "Viagem e lazer", "img": "Banco de Imagens/Cadeira Camping/1.png"}
    ]
    
    # We add animate-on-scroll logic with staggered delays
    # The reference uses: class="animate-on-scroll [animation:animationIn_0.8s_ease-out_0s_both]"
    
    new_html = start_marker + "\n"
    new_html += '            <div class="flex overflow-x-auto gap-6 md:gap-8 pb-12 snap-x hide-scrollbar px-4 md:px-0" style="scrollbar-width: none;">\n'
    
    for i, cat in enumerate(cats):
        delay = i * 0.15
        
        card_html = f"""
                <!-- Cat {i+1} -->
                <a href="#" class="min-w-[280px] w-[280px] md:min-w-[0] md:flex-1 group cursor-hover snap-center relative p-[1px] rounded-2xl transition-all duration-700 hover:-translate-y-3 hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.1)] reveal-up" style="transition-delay: {delay}s;">
                    
                    <!-- Spinning Border Beam (Visible on Hover) from reference -->
                    <span class="absolute inset-[-100%] animate-[spin_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,transparent_0%,transparent_75%,rgba(0,0,0,0.15)_100%)] opacity-0 transition-opacity duration-500 group-hover:opacity-100 rounded-full"></span>
                    
                    <!-- Card Background and Flashlight Effect -->
                    <div class="relative w-full h-full flex flex-col bg-white z-10 flashlight-card-light overflow-hidden rounded-2xl ring-1 ring-black/5" onmousemove="const rect = this.getBoundingClientRect(); this.style.setProperty('--mouse-x', `${{event.clientX - rect.left}}px`); this.style.setProperty('--mouse-y', `${{event.clientY - rect.top}}px`);">
                        
                        <!-- Internal Gradient / Subtle Background Texture -->
                        <div class="absolute inset-0 bg-gradient-to-br from-stone-50 to-stone-100 opacity-50 pointer-events-none"></div>

                        <div class="w-full aspect-[4/5] overflow-hidden relative flex items-center justify-center p-8">
                            
                            <!-- Premium Image Animation: zoom on hover, subtle floating -->
                            <img src="{cat['img']}" class="w-full h-full object-contain mix-blend-multiply group-hover:scale-110 group-hover:-translate-y-2 transition-transform duration-[800ms] ease-[cubic-bezier(0.25,1,0.5,1)] relative z-10" alt="{cat['name']}">
                            
                            <!-- Glass Panel Label (Premium UI) -->
                            <div class="absolute bottom-4 left-4 right-4 bg-white/80 backdrop-blur-xl border border-white/60 py-4 px-6 text-center transform translate-y-4 opacity-90 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-[600ms] ease-[cubic-bezier(0.16,1,0.3,1)] shadow-[0_8px_30px_rgb(0,0,0,0.06)] rounded-xl flex items-center justify-between overflow-hidden z-20">
                                <span class="font-body text-xs md:text-sm text-dark font-semibold tracking-wider uppercase z-10">{cat['name']}</span>
                                
                                <!-- Hover Arrow Animation -->
                                <div class="w-6 h-6 rounded-full bg-dark flex items-center justify-center opacity-0 -translate-x-4 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-500 delay-100">
                                    <svg class="w-3 h-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg>
                                </div>
                            </div>
                        </div>
                    </div>
                </a>
"""
        new_html += card_html
        
    new_html += '            </div>\n            '
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(pre + new_html + post)
    print("Done replacing.")
else:
    print("Markers not found.")
