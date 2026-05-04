import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Vitrines Containers
# Mais Vendidos
# Current: <div class="flex gap-6 md:gap-8 overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-12 pt-4 reveal-up" id="maisVendidosCarouselContainer" style="scrollbar-width: none;">
content = content.replace(
    '<div class="flex gap-6 md:gap-8 overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-12 pt-4 reveal-up" id="maisVendidosCarouselContainer" style="scrollbar-width: none;">',
    '<div class="flex md:grid md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-8 overflow-x-auto md:overflow-x-visible snap-x snap-mandatory md:snap-none hide-scrollbar pb-12 pt-4 reveal-up" id="maisVendidosCarouselContainer" style="scrollbar-width: none;">'
)

# Categorias Container (Section 2)
content = content.replace(
    '<div id="categoriasCarouselContainer" class="flex overflow-x-auto gap-6 md:gap-8 pb-12 snap-x hide-scrollbar px-4 md:px-0" style="scrollbar-width: none;">',
    '<div id="categoriasCarouselContainer" class="flex md:grid md:grid-cols-2 lg:grid-cols-4 overflow-x-auto md:overflow-x-visible gap-4 md:gap-8 pb-12 snap-x snap-mandatory md:snap-none hide-scrollbar px-4 md:px-0" style="scrollbar-width: none;">'
)

# Viagem & Lazer
content = content.replace(
    '<div class="flex gap-6 md:gap-8 overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-16 pt-4" id="lancamentosCarouselContainer" style="scrollbar-width: none;">',
    '<div class="flex md:grid md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-8 overflow-x-auto md:overflow-x-visible snap-x snap-mandatory md:snap-none hide-scrollbar pb-16 pt-4" id="lancamentosCarouselContainer" style="scrollbar-width: none;">'
)

# 2. Hide Desktop Carousel Arrows (since they are now Grids on desktop)
content = content.replace(
    '<div class="hidden md:flex items-center gap-4 mt-6 md:mt-0">',
    '<div class="hidden items-center gap-4 mt-6 md:mt-0">'
) # Hide completely so they don't show up on desktop grids

# 3. Update Product Cards Width (to show 1.2-1.5 cards on mobile)
# Currently: class="min-w-[280px] md:min-w-[320px] w-[280px] md:w-[320px]
# Mobile standard view for ~1.3 cards on 375px screen is roughly 280px.
# But we can make it `min-w-[75vw] w-[75vw] md:min-w-0 md:w-full` for the grid to work properly on desktop!
# Wait! If it's a grid on desktop, the cards MUST NOT have fixed width like `w-[320px]`. They must be `md:w-full md:min-w-0`.
content = content.replace(
    'class="min-w-[280px] md:min-w-[320px] w-[280px] md:w-[320px] group',
    'class="min-w-[75vw] w-[75vw] md:min-w-0 md:w-full group'
)

# Categorias cards are currently:
# class="min-w-[280px] w-[280px] md:min-w-[0] md:flex-1 group 
content = content.replace(
    'class="min-w-[280px] w-[280px] md:min-w-[0] md:flex-1 group',
    'class="min-w-[75vw] w-[75vw] md:min-w-0 md:w-full md:flex-1 group'
)

# 4. Touch Targets for Cart Buttons (min 44x44)
content = content.replace(
    '<div class="w-10 h-10 rounded-full bg-dark text-white flex items-center justify-center hover:bg-accent transition-colors group-hover:scale-110 group-hover:shadow-lg">',
    '<div class="w-11 h-11 md:w-10 md:h-10 rounded-full bg-dark text-white flex items-center justify-center hover:bg-accent transition-colors md:group-hover:scale-110 md:group-hover:shadow-lg">'
)
content = content.replace(
    '<div class="w-10 h-10 rounded-full border border-dark/20 text-dark flex items-center justify-center hover:bg-dark hover:text-white transition-colors group-hover:scale-110 group-hover:shadow-lg">',
    '<div class="w-11 h-11 md:w-10 md:h-10 rounded-full border border-dark/20 text-dark flex items-center justify-center hover:bg-dark hover:text-white transition-colors md:group-hover:scale-110 md:group-hover:shadow-lg">'
)

# 5. Fix Hover states for Mobile (Mini Carousel Arrows)
# Make arrows always visible on mobile, hide them on desktop until hover
content = content.replace(
    'opacity-0 group-hover/slider:opacity-100 transition-opacity',
    'opacity-100 md:opacity-0 md:group-hover/slider:opacity-100 transition-opacity'
)

# Fix Category Cards "Conheça" arrow which only animates on hover
# Ensure it looks good on mobile without hover
content = content.replace(
    'group-hover:translate-x-1.5 transition-transform duration-300',
    'md:group-hover:translate-x-1.5 transition-transform duration-300'
)

# Also fix the line-clamp / title hover color
content = content.replace(
    'group-hover:text-accent transition-colors line-clamp-2',
    'md:group-hover:text-accent transition-colors line-clamp-2'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Card optimization complete!")
