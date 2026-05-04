import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Adjust Vertical Rhythm (Spacing)
# We want to replace standard py-24 with py-16 md:py-24, py-32 with py-20 md:py-32, etc.
# But we must be careful not to duplicate if it already has responsive prefixes.

replacements = {
    'class="py-24 ': 'class="py-16 md:py-24 ',
    'class="py-32 ': 'class="py-20 md:py-32 ',
    'class="pb-24 ': 'class="pb-16 md:pb-24 ',
    'class="pb-32 ': 'class="pb-20 md:pb-32 ',
    'class="mb-20 ': 'class="mb-12 md:mb-20 ',
    'class="mb-12 ': 'class="mb-8 md:mb-12 '
}

for old, new in replacements.items():
    html = html.replace(old, new)

# 2. Add Mobile Sticky CTA and adjust Footer padding
footer_tag = '<footer class="w-full bg-[#0A0A0A] text-white pt-20 pb-8 px-6 md:px-12 lg:px-20 border-t border-white/10 relative z-10">'
new_footer_tag = '<footer class="w-full bg-[#0A0A0A] text-white pt-20 pb-24 md:pb-8 px-6 md:px-12 lg:px-20 border-t border-white/10 relative z-10">'
html = html.replace(footer_tag, new_footer_tag)

sticky_cta = '''
    <!-- Mobile Sticky CTA -->
    <div class="fixed bottom-0 left-0 w-full bg-white border-t border-dark/10 p-4 pb-6 z-[60] md:hidden shadow-[0_-10px_30px_rgba(0,0,0,0.08)] transform transition-transform duration-300" id="mobileStickyCta">
        <a href="https://www.amazon.com.br/s?me=A2FL1W3S46MFWA&marketplaceID=A2Q3Y263D00KWC" target="_blank" rel="noopener noreferrer" class="w-full h-12 bg-accent text-white font-mono text-[11px] uppercase tracking-[0.15em] font-bold rounded-full flex items-center justify-center shadow-lg hover:bg-dark transition-colors active:scale-95">
            Ver Ofertas na Amazon
        </a>
    </div>

</body>
'''
html = html.replace('</body>', sticky_cta)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML spacing and CTA.")
