import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the image mapping
img_map = {
    "Organizador de Pia em Aço Carbono Preto": ["img/produtos/Suporte Pia/1.png", "img/produtos/Suporte Pia/2.png", "img/produtos/Suporte Pia/3.png"],
    "Kit 2 Potes Herméticos 1,5L com Medidor": ["img/produtos/Potes Herméticos Tampa Bambu/1.png", "img/produtos/Potes Herméticos Tampa Bambu/2.png", "img/produtos/Potes Herméticos Tampa Bambu/3.png"],
    "Chaleira de Vidro Borossilicato 950ml com Infusor": ["img/produtos/Chaleira Infusor/1.png", "img/produtos/Chaleira Infusor/2.png", "img/produtos/Chaleira Infusor/3.png"],
    "Pote Hermético 1L de Vidro Borossilicato": ["img/produtos/Potes Herméticos Tampa Bambu/4.png", "img/produtos/Potes Herméticos Tampa Bambu/5.png", "img/produtos/Potes Herméticos Tampa Bambu/6.png"],
    "Kit 2 Potes Herméticos 1L de Vidro e Bambu": ["img/produtos/Potes Herméticos Tampa Bambu/7.png", "img/produtos/Potes Herméticos Tampa Bambu/8.png", "img/produtos/Potes Herméticos Tampa Bambu/9.png"],
    "Kit 4 Potes Herméticos 1,5L com Medidor": ["img/produtos/Potes Herméticos Tampa Bambu/10.png", "img/produtos/Potes Herméticos Tampa Bambu/11.png", "img/produtos/Potes Herméticos Tampa Bambu/12.png"],
    "Organizador de Gavetas Modular Transparente (7 Peças)": ["img/produtos/Kit 7 organizadores/1.png", "img/produtos/Kit 7 organizadores/2.png", "img/produtos/Kit 7 organizadores/3.png"]
}

# The cards are inside <a ... class="... group ...">
# We want to add the premium shimmer to the card.
# <div class="absolute inset-0 -translate-x-full bg-gradient-to-r from-transparent via-white/50 to-transparent group-hover:animate-[shimmer-light_1.5s_infinite] pointer-events-none z-30"></div>
# Let's just find the start of each card.
# The card starts with <a href="https://www.amazon.com.br/dp/...
# And has the title in <h3 ...>TITLE</h3>
# We can find each card block by splitting by '<a href="https://www.amazon.com.br/dp/'

parts = content.split('<a href="https://www.amazon.com.br/dp/')
for i in range(1, len(parts)):
    part = parts[i]
    # Check if this part has a title from our img_map
    for title, images in img_map.items():
        if f'>{title}</h3>' in part:
            # Replace placeholders
            part = part.replace('[Placeholder Imagem 1]', images[0])
            part = part.replace('[Placeholder Imagem 2]', images[1])
            part = part.replace('[Placeholder Imagem 3]', images[2])
            
            # Add shimmer and interactive premium CSS
            # We will insert the shimmer div right after the opening <a> tag closes.
            # The <a> tag ends at the first '>' that is not inside quotes.
            # Actually, we can find 'hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)]">'
            
            if 'hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)]">' in part:
                # Add flashlight class and more premium shadow
                part = part.replace('hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)]">', 
                                    'hover:shadow-[0_30px_60px_-15px_rgba(0,0,0,0.12)] flashlight-card-light" onmousemove="const rect = this.getBoundingClientRect(); this.style.setProperty(\'--mouse-x\', `${event.clientX - rect.left}px`); this.style.setProperty(\'--mouse-y\', `${event.clientY - rect.top}px`);">\n                    <!-- Premium Shimmer -->\n                    <div class="absolute inset-0 -translate-x-full bg-gradient-to-r from-transparent via-white/50 to-transparent group-hover:animate-[shimmer-light_1.5s_infinite] pointer-events-none z-30 rounded-[2rem] overflow-hidden"></div>')
            
            parts[i] = part
            break

content = '<a href="https://www.amazon.com.br/dp/'.join(parts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated images and added premium effects!")
