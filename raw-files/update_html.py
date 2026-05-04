import json
import re

with open('products.json') as f:
    products = json.load(f)

# Group products
cozinha = [p for p in products if p['categoria'] == 'Cozinha']
casa_org = [p for p in products if p['categoria'] in ['Casa', 'Organização']]
camping = [p for p in products if p['categoria'] == 'Camping & Lazer']

def generate_card(p, style='grid'):
    # style='grid' for section 3, style='carousel' for section 5, style='carousel-glow' for section 5.5
    
    # ensure we have at least 1 image
    imgs = p['imagens']
    if not imgs:
        imgs = ['https://via.placeholder.com/600']
    
    main_img = imgs[0]
    sec_imgs = imgs[:5] # fotos 1 a 5
    
    thumbnails_html = ""
    if len(sec_imgs) > 1:
        thumbs = "".join([f'<img src="{i}" class="w-8 h-8 md:w-10 md:h-10 object-cover rounded cursor-pointer border border-transparent hover:border-accent transition-colors shadow-sm" onmouseover="this.parentElement.parentElement.querySelector(\'.main-img\').src=\'{i}\'">' for i in sec_imgs])
        thumbnails_html = f"""
        <div class="absolute bottom-2 left-1/2 -translate-x-1/2 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-white/80 backdrop-blur-md p-1.5 rounded-xl z-20 shadow-lg">
             {thumbs}
        </div>
        """
    
    if style == 'grid':
        return f"""
                <div class="group cursor-hover">
                    <div class="w-full aspect-square bg-white relative overflow-hidden flex items-center justify-center mb-4 p-4 border border-dark/5">
                        <img src="{main_img}" class="main-img w-full h-full object-contain mix-blend-multiply group-hover:scale-105 transition-transform duration-500" alt="{p['nome']}">
                        {thumbnails_html}
                    </div>
                    
                    <div class="px-2">
                        <h3 class="font-body text-sm text-dark font-medium mb-1 line-clamp-2 min-h-[40px]">{p['nome']}</h3>
                        <div class="flex items-center gap-1 text-dark/40 mb-3">
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                        </div>
                        <div class="flex justify-between items-end">
                            <span class="font-display font-bold text-dark">{p['preco']}</span>
                            <button class="text-dark/50 hover:text-accent transition-colors">
                                <i data-lucide="shopping-bag" class="w-5 h-5"></i>
                            </button>
                        </div>
                    </div>
                </div>
"""
    elif style == 'carousel':
        return f"""
                <div class="min-w-[280px] md:min-w-[320px] w-[280px] md:w-[320px] group cursor-hover snap-start flashlight-card-light relative border border-dark/5 hover:border-dark/10 bg-white transition-all duration-500 overflow-hidden" 
                     onmousemove="const rect = this.getBoundingClientRect(); this.style.setProperty('--mouse-x', `${{event.clientX - rect.left}}px`); this.style.setProperty('--mouse-y', `${{event.clientY - rect.top}}px`);">
                    <div class="w-full aspect-[4/5] bg-white relative overflow-hidden flex items-center justify-center p-6 border-b border-dark/5">
                        <img src="{main_img}" class="main-img w-full h-full object-contain mix-blend-multiply group-hover:scale-105 transition-transform duration-700" alt="{p['nome']}">
                        {thumbnails_html}
                    </div>
                    <div class="px-6 py-6 bg-white">
                        <h3 class="font-body text-base text-dark font-medium leading-tight mb-2 group-hover:text-accent transition-colors line-clamp-2">{p['nome']}</h3>
                        <div class="flex justify-between items-end mt-4">
                            <div class="flex flex-col">
                                <span class="font-display font-bold text-lg text-dark">{p['preco']}</span>
                            </div>
                            <button class="w-10 h-10 rounded-full bg-dark text-white flex items-center justify-center hover:bg-accent transition-colors group-hover:scale-110">
                                <i data-lucide="shopping-cart" class="w-4 h-4"></i>
                            </button>
                        </div>
                    </div>
                </div>
"""
    elif style == 'carousel-glow':
        return f"""
                <div class="min-w-[300px] md:min-w-[380px] w-[300px] md:w-[380px] group cursor-hover snap-start relative p-[1px] rounded-2xl overflow-hidden flashlight-card-light"
                     onmousemove="const rect = this.getBoundingClientRect(); this.style.setProperty('--mouse-x', `${{event.clientX - rect.left}}px`); this.style.setProperty('--mouse-y', `${{event.clientY - rect.top}}px`);">
                    <!-- Shimmer Beam -->
                    <div class="absolute -inset-[1px] overflow-hidden opacity-0 group-hover:opacity-100 transition duration-500 pointer-events-none">
                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[300%] h-[300%] bg-[conic-gradient(from_0deg,transparent_0_340deg,#374336_360deg)] animate-[spin_4s_linear_infinite]"></div>
                    </div>
                    
                    <div class="relative w-full h-full flex flex-col bg-stone/50 backdrop-blur-md z-10 border border-dark/5 rounded-2xl overflow-hidden shadow-[0_10px_30px_-10px_rgba(0,0,0,0.1)] hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.15)] transition-shadow duration-500">
                        <div class="absolute top-4 left-4 z-20">
                            <span class="px-3 py-1 bg-white border border-dark/10 rounded-full font-mono text-[9px] uppercase tracking-wider text-dark font-bold shadow-sm">Camping & Lazer</span>
                        </div>
                        
                        <div class="w-full aspect-square relative overflow-hidden bg-white/80 p-8 flex items-center justify-center border-b border-dark/5">
                            <div class="absolute inset-0 bg-gradient-to-br from-white/40 to-transparent pointer-events-none z-10"></div>
                            
                            <!-- Diagonal Glass Glare -->
                            <div class="absolute top-0 left-[-100%] w-1/2 h-full bg-gradient-to-r from-transparent via-white/40 to-transparent skew-x-[-20deg] group-hover:animate-[shimmer-light_2s_ease-out_infinite] z-20 pointer-events-none"></div>
                            
                            <img src="{main_img}" class="main-img w-full h-full object-contain mix-blend-multiply group-hover:scale-110 transition-transform duration-700 relative z-0" alt="{p['nome']}">
                            {thumbnails_html}
                        </div>
                        
                        <div class="p-6 md:p-8 flex-1 flex flex-col justify-between bg-white/90 relative z-10">
                            <div>
                                <h3 class="font-display text-lg md:text-xl font-bold text-dark mb-2 leading-tight group-hover:text-accent transition-colors line-clamp-2">{p['nome']}</h3>
                                <div class="w-8 h-[2px] bg-dark/10 mb-4 group-hover:w-16 group-hover:bg-accent transition-all duration-500"></div>
                            </div>
                            
                            <div class="flex items-center justify-between mt-auto pt-4">
                                <span class="font-body font-light text-xl text-dark tracking-tight">{p['preco']}</span>
                                <button class="group/btn relative flex items-center justify-center w-10 h-10 rounded-full border border-dark/20 text-dark hover:border-transparent hover:text-white overflow-hidden transition-colors">
                                    <span class="absolute inset-0 bg-dark transform scale-0 group-hover/btn:scale-100 transition-transform duration-300 rounded-full z-0"></span>
                                    <i data-lucide="plus" class="w-5 h-5 relative z-10"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
"""


with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# SECTION 3: Cozinha
sec3_products = "".join([generate_card(p, 'grid') for p in cozinha])
content = re.sub(r'(<!-- SECTION 3:.*?<h2[^>]*>).*?(</h2>\s*<p[^>]*>).*?(</p>)', rf'\g<1>Cozinha\g<2>Utensílios e organizadores para sua rotina\g<3>', content, flags=re.DOTALL)
content = re.sub(r'(<!-- Products Grid -->\s*<div[^>]*>).*?(?=</div>\s*</div>\s*</section>)', rf'\g<1>{sec3_products}', content, flags=re.DOTALL)


# SECTION 5: Casa & Organização
sec5_products = "".join([generate_card(p, 'carousel') for p in casa_org])
content = re.sub(r'(<!-- SECTION 5:.*?<h2[^>]*>).*?(</h2>\s*<p[^>]*>).*?(</p>)', rf'\g<1>Casa & Organização\g<2>Soluções inteligentes para cada ambiente\g<3>', content, flags=re.DOTALL)
content = re.sub(r'(<!-- Products Carousel -->\s*<div[^>]*>).*?(?=\s*</div>\s*</div>\s*</section>)', rf'\g<1>{sec5_products}', content, flags=re.DOTALL)


# SECTION 5.5: Camping & Lazer
sec55_products = "".join([generate_card(p, 'carousel-glow') for p in camping])
content = re.sub(r'(<!-- SECTION 5\.5:.*?<h2[^>]*>).*?(</h2>\s*<p[^>]*>).*?(</p>)', rf'\g<1>Camping & Lazer\g<2>Praticidade e conforto em qualquer lugar\g<3>', content, flags=re.DOTALL)
content = re.sub(r'(<div class="flex gap-6 overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-12 w-full" id="lancamentosCarouselContainer">).*?(?=\s*</div>\s*</div>\s*</section>)', rf'\g<1>{sec55_products}', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
