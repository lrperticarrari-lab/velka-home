import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# --- DOBRA 2 (Categorias) ---
s2_start = content.find("<!-- Categories Grid/Carousel -->")
s3_start = content.find("<!-- SECTION 3: MAIS VENDIDOS -->")

if s2_start != -1 and s3_start != -1:
    s2_content = content[s2_start:s3_start]
    
    # Add target="_blank" and rel="noopener noreferrer" to category links
    s2_content = s2_content.replace('<a href="#" class="', '<a href="https://www.amazon.com.br" target="_blank" rel="noopener noreferrer" class="')
    
    # Replace the images with Unsplash lifestyle images
    # We'll use specific Unsplash URLs and remove padding/mix-blend
    
    images_map = [
        ("Banco de Imagens/Potes Herméticos Tampa Bambu/1.png", "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?q=80&w=800&auto=format&fit=crop"), # Pantry
        ("Banco de Imagens/Suporte Toalhas/1.png", "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=800&auto=format&fit=crop"), # Bathroom
        ("Banco de Imagens/Kit organizadores gaveta/1.png", "https://images.unsplash.com/photo-1595526114101-11b0e501a3cd?q=80&w=800&auto=format&fit=crop"), # Living room boxes
        ("Banco de Imagens/Bandeja decorativa/1.png", "https://images.unsplash.com/photo-1577140917170-285929fb55b7?q=80&w=800&auto=format&fit=crop"), # Set table
        ("Banco de Imagens/Cadeira Camping/1.png", "https://images.unsplash.com/photo-1553901753-215db0446d9a?q=80&w=800&auto=format&fit=crop") # Travel
    ]
    
    # Also change the style of the images
    # Old class: "w-full h-full object-contain mix-blend-multiply group-hover:scale-110 group-hover:-translate-y-2 transition-transform duration-[800ms] ease-[cubic-bezier(0.25,1,0.5,1)] relative z-10"
    # New class: "w-full h-full object-cover group-hover:scale-110 group-hover:-translate-y-2 transition-transform duration-[800ms] ease-[cubic-bezier(0.25,1,0.5,1)] relative z-10"
    
    for old_src, new_src in images_map:
        s2_content = s2_content.replace(f'src="{old_src}" class="w-full h-full object-contain mix-blend-multiply', f'src="{new_src}" class="w-full h-full object-cover')
        
    content = content[:s2_start] + s2_content + content[s3_start:]

# --- DOBRA 3 (Mais Vendidos) ---
s3_start = content.find("<!-- SECTION 3: MAIS VENDIDOS -->")
s4_start = content.find("<!-- SECTION 4: CARROSSEL DIA DAS MÃES -->")

if s3_start != -1 and s4_start != -1:
    s3_content = content[s3_start:s4_start]
    
    # 1. Update Title and Subtitle
    s3_content = s3_content.replace('>Cozinha<', '>Mais Vendidos<')
    s3_content = s3_content.replace('>Utensílios e organizadores para sua rotina<', '>Os produtos favoritos para facilitar o seu dia a dia.<')
    
    # 2. Change product <div class="group cursor-hover..."> to <a href="...">
    target_div = '<div class="group cursor-hover relative flex flex-col p-3 rounded-3xl transition-all duration-700 hover:-translate-y-3 hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)] bg-transparent hover:bg-white border border-transparent hover:border-dark/5">'
    replacement_a = '<a href="https://www.amazon.com.br" target="_blank" rel="noopener noreferrer" class="group cursor-hover relative flex flex-col p-3 rounded-3xl transition-all duration-700 hover:-translate-y-3 hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)] bg-transparent hover:bg-white border border-transparent hover:border-dark/5">'
    
    # 3. Change closing </div> to </a> for the product cards.
    # Since we can't easily distinguish the closing div of the card from other inner divs via simple replace,
    # we'll do it using regex to match the block structure.
    
    # Actually, a better way: 
    # Find all product blocks and replace the tags.
    # The block ends after the "px-2" div.
    
    # Let's split by the target_div
    parts = s3_content.split(target_div)
    new_s3_content = parts[0]
    for part in parts[1:]:
        # Each 'part' contains the inside of the product card, ending with '</div>\n\n' and then the next product or closing grid div.
        # Let's find the last '</div>' in this 'part' before the next blank line or next target.
        # Wait, the structure inside the card has 2 main divs: the image container and the "px-2" text container.
        # It ends with:
        #             </div>
        #         </div>  <-- this is the one we want to turn into </a>
        
        # Let's replace the last </div> before a bunch of spaces and the end of 'part'
        # To be safe, we can use a reverse search
        idx = part.rfind('</div>\n')
        if idx != -1:
            # Check if this is the outer div
            part = part[:idx] + '</a>\n' + part[idx+7:]
        
        new_s3_content += replacement_a + part
        
    # Let's write it back
    content = content[:s3_start] + new_s3_content + content[s4_start:]


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Dobras 2 and 3")
