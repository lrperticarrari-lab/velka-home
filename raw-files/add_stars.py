import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s5_start = content.find("<!-- SECTION 5: KITS ESSENCIAIS -->")
s6_start = content.find("<!-- SECTION 6: NEWSLETTER & AVALIAÇÕES -->")

if s5_start != -1 and s6_start != -1:
    s5_content = content[s5_start:s6_start]
    
    # We want to find </h3> inside the product descriptions.
    # The h3 tag format is: <h3 class="font-body text-base text-dark font-medium leading-tight mb-2 group-hover:text-accent transition-colors line-clamp-2">...</h3>
    
    stars_html = '''</h3>
                        <div class="flex items-center gap-1 text-dark/40 mb-3">
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                            <i data-lucide="star" class="w-3 h-3 fill-current text-dark/80"></i>
                        </div>'''
                        
    # Replace </h3> with </h3> + stars if it hasn't been added yet
    # To be safe, we only replace it if it's inside the <div class="px-6 py-6 bg-white">
    # Actually, we can just replace </h3> with the new string globally within s5_content because all h3s in this section are product titles!
    
    s5_content = s5_content.replace('</h3>', stars_html)
    
    content = content[:s5_start] + s5_content + content[s6_start:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added star ratings to Casa & Organização.")
