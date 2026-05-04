import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Split the doc into parts:
head_nav_match = re.search(r'(<html.*?</nav>)', text, re.DOTALL)
hero_match = re.search(r'(<!-- Hero Section -->.*?<!-- Ecosystem Stats -->)', text, re.DOTALL)
footer_match = re.search(r'(<!-- Footer -->.*</html>)', text, re.DOTALL)

head_nav = head_nav_match.group(1) if head_nav_match else ""
hero = hero_match.group(1) if hero_match else ""
footer = footer_match.group(1) if footer_match else ""
footer = footer.replace("<!-- Footer -->", "<!-- Footer -->\n")

# Modify Nav
nav_replacement = """
<nav class="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-neutral-100">
<div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
<div class="flex items-center gap-2">
<div class="w-8 h-8 rounded-full bg-[#ccf32f] flex items-center justify-center">
<i class="w-4 h-4 text-black" data-lucide="layers"></i>
</div>
<span class="text-lg font-medium tracking-tight">DESIGN SYSTEM</span>
</div>
<div class="hidden md:flex flex-wrap items-center gap-4 text-sm font-medium text-neutral-500">
<a class="hover:text-black transition-colors" href="#hero">Hero</a>
<a class="hover:text-black transition-colors" href="#typography">Typography</a>
<a class="hover:text-black transition-colors" href="#colors">Colors & Surfaces</a>
<a class="hover:text-black transition-colors" href="#components">UI Components</a>
<a class="hover:text-black transition-colors" href="#layout">Layout</a>
<a class="hover:text-black transition-colors" href="#motion">Motion</a>
<a class="hover:text-black transition-colors" href="#icons">Icons</a>
</div>
</div>
</nav>
"""
head_nav = re.sub(r'<nav.*?</nav>', nav_replacement, head_nav, flags=re.DOTALL)

# Modify Hero
hero = hero.replace('A liberdade para <br/>\n                        ensinar e aprender.', 'Design System <br/>\n                        & Pattern Library.')
hero = hero.replace('Conectamos alunos a instrutores independentes e frotas homologadas. Menos burocracia, mais economia e total autonomia baseada na nova lei CNH.', 'Uma documentação viva com os tokens, estilos e componentes oficiais deste projeto. Pronta para escalar.')
hero = hero.replace('Quero me cadastrar', 'Explorar os Componentes')
hero = hero.replace('Entenda a Resolução 1.020', 'Ver Tipografia e Cores')
hero = hero.replace('href="#lista-espera"', 'href="#components"')
hero = hero.replace('href="#faq"', 'href="#typography"')
# wrap hero in a section with id
hero = '<section id="hero">\n' + hero.replace('<!-- Ecosystem Stats -->', '') + '</section>\n'

# Adding the extra sections
extra_sections = """
<section id="typography" class="max-w-7xl mx-auto px-6 py-24 border-b border-neutral-100">
    <div class="mb-16">
        <h2 class="text-3xl md:text-5xl font-medium tracking-tight">1. Typography</h2>
        <p class="text-lg text-neutral-500 mt-4 max-w-2xl">Hierarchy, scale, and rhythm.</p>
    </div>
    <div class="space-y-12">
        <div class="flex flex-col md:flex-row md:items-baseline justify-between border-b border-neutral-100 pb-8 gap-4">
            <div class="w-48 shrink-0 text-sm font-medium text-neutral-400">Heading 1</div>
            <div class="flex-1"><h1 class="text-4xl md:text-6xl font-medium tracking-tight leading-[1.1]">The quick brown fox</h1></div>
            <div class="text-sm font-medium text-neutral-400 md:text-right shrink-0">60px / 1.1</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-baseline justify-between border-b border-neutral-100 pb-8 gap-4">
            <div class="w-48 shrink-0 text-sm font-medium text-neutral-400">Heading 2</div>
            <div class="flex-1"><h2 class="text-3xl md:text-5xl font-medium tracking-tight">The quick brown fox</h2></div>
            <div class="text-sm font-medium text-neutral-400 md:text-right shrink-0">48px</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-baseline justify-between border-b border-neutral-100 pb-8 gap-4">
            <div class="w-48 shrink-0 text-sm font-medium text-neutral-400">Heading 3</div>
            <div class="flex-1"><h3 class="text-2xl md:text-3xl font-medium tracking-tight">The quick brown fox</h3></div>
            <div class="text-sm font-medium text-neutral-400 md:text-right shrink-0">30px</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-baseline justify-between border-b border-neutral-100 pb-8 gap-4">
            <div class="w-48 shrink-0 text-sm font-medium text-neutral-400">Heading 4</div>
            <div class="flex-1"><h4 class="text-lg md:text-xl font-medium tracking-tight">The quick brown fox</h4></div>
            <div class="text-sm font-medium text-neutral-400 md:text-right shrink-0">20px</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-baseline justify-between border-b border-neutral-100 pb-8 gap-4">
            <div class="w-48 shrink-0 text-sm font-medium text-neutral-400">Paragraph L</div>
            <div class="flex-1"><p class="text-xl md:text-2xl font-normal text-neutral-800 leading-relaxed">The quick brown fox jumps over the lazy dog.</p></div>
            <div class="text-sm font-medium text-neutral-400 md:text-right shrink-0">24px</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-baseline justify-between border-b border-neutral-100 pb-8 gap-4">
            <div class="w-48 shrink-0 text-sm font-medium text-neutral-400">Paragraph M</div>
            <div class="flex-1"><p class="text-lg font-normal text-neutral-500 leading-relaxed">The quick brown fox jumps over the lazy dog.</p></div>
            <div class="text-sm font-medium text-neutral-400 md:text-right shrink-0">18px</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-baseline justify-between border-b border-neutral-100 pb-8 gap-4">
            <div class="w-48 shrink-0 text-sm font-medium text-neutral-400">Paragraph S</div>
            <div class="flex-1"><p class="text-base font-normal text-neutral-500 leading-relaxed">The quick brown fox jumps over the lazy dog.</p></div>
            <div class="text-sm font-medium text-neutral-400 md:text-right shrink-0">16px</div>
        </div>
        <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-4">
            <div class="w-48 shrink-0 text-sm font-medium text-neutral-400">Small Text</div>
            <div class="flex-1"><p class="text-sm font-normal text-neutral-500">The quick brown fox</p></div>
            <div class="text-sm font-medium text-neutral-400 md:text-right shrink-0">14px</div>
        </div>
    </div>
</section>

<section id="colors" class="max-w-7xl mx-auto px-6 py-24 border-b border-neutral-100">
    <div class="mb-16">
        <h2 class="text-3xl md:text-5xl font-medium tracking-tight">2. Colors & Surfaces</h2>
        <p class="text-lg text-neutral-500 mt-4 max-w-2xl">Brand colors, neutral scales, and elevation layers.</p>
    </div>
    <div class="space-y-12">
        <div>
            <h3 class="text-xl font-medium mb-6">Brand / Accents</h3>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-6">
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-[#ccf32f] border border-neutral-100 shadow-sm flex items-end p-4">
                        <span class="text-black font-medium">#ccf32f</span>
                    </div>
                    <div>
                        <div class="font-medium">Primary Accent</div>
                        <div class="text-sm text-neutral-500">bg-[#ccf32f]</div>
                    </div>
                </div>
            </div>
        </div>
        <div>
            <h3 class="text-xl font-medium mb-6">Neutrals</h3>
            <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6">
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-white border border-neutral-200 shadow-sm"></div>
                    <div><div class="font-medium">White</div><div class="text-sm text-neutral-500">bg-white</div></div>
                </div>
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-neutral-50 border border-neutral-200 shadow-sm"></div>
                    <div><div class="font-medium">Neutral 50</div><div class="text-sm text-neutral-500">bg-neutral-50</div></div>
                </div>
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-neutral-100 border border-neutral-200 shadow-sm"></div>
                    <div><div class="font-medium">Neutral 100</div><div class="text-sm text-neutral-500">bg-neutral-100</div></div>
                </div>
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-neutral-200 border border-neutral-300 shadow-sm"></div>
                    <div><div class="font-medium">Neutral 200</div><div class="text-sm text-neutral-500">bg-neutral-200</div></div>
                </div>
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-neutral-800 border border-neutral-800 shadow-sm"></div>
                    <div><div class="font-medium">Neutral 800</div><div class="text-sm text-neutral-500">bg-neutral-800</div></div>
                </div>
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-black border border-black shadow-sm"></div>
                    <div><div class="font-medium">Black</div><div class="text-sm text-neutral-500">bg-black</div></div>
                </div>
            </div>
        </div>
        <div>
            <h3 class="text-xl font-medium mb-6">Surfaces & Glass</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 p-8 bg-[#ccf32f]/20 rounded-[2.5rem]">
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-white/80 backdrop-blur-md border px-4 py-3 flex items-start text-sm">
                        Content under blur...
                    </div>
                    <div><div class="font-medium">Light Glass</div><div class="text-sm text-neutral-500">bg-white/80<br>backdrop-blur-md</div></div>
                </div>
                <div class="space-y-3">
                    <div class="h-32 rounded-2xl bg-black/60 backdrop-blur-sm px-4 py-3 border border-neutral-800 flex items-start text-sm text-white">
                        Content under blur...
                    </div>
                    <div><div class="font-medium">Dark Glass</div><div class="text-sm text-neutral-500">bg-black/60<br>backdrop-blur-sm</div></div>
                </div>
            </div>
        </div>
    </div>
</section>

<section id="components" class="max-w-7xl mx-auto px-6 py-24 border-b border-neutral-100 bg-neutral-50/50">
    <div class="mb-16">
        <h2 class="text-3xl md:text-5xl font-medium tracking-tight">3. UI Components</h2>
        <p class="text-lg text-neutral-500 mt-4 max-w-2xl">Interactive elements, buttons, and cards.</p>
    </div>
    <div class="space-y-16">
        <div>
            <h3 class="text-xl font-medium mb-6">Buttons</h3>
            <div class="flex flex-wrap items-center gap-6 p-8 bg-white rounded-3xl border border-neutral-100">
                <div class="space-y-3">
                    <p class="text-sm text-neutral-400 font-medium">Dark Pill (Hero)</p>
                    <a class="bg-black text-white text-base font-medium px-7 py-3.5 rounded-full hover:bg-neutral-800 transition-transform hover:scale-105 flex items-center gap-2 w-max" href="#!">
                        <i class="w-5 h-5" data-lucide="clipboard-list"></i>
                        Quero me cadastrar
                    </a>
                </div>
                <div class="space-y-3">
                    <p class="text-sm text-neutral-400 font-medium">Outline Pill (Nav)</p>
                    <a class="text-base font-medium flex items-center gap-2 group hover:text-neutral-700 w-max" href="#!">
                        <div class="w-8 h-8 rounded-full border-2 border-black flex items-center justify-center">
                            <i class="w-4 h-4 ml-0.5" data-lucide="info"></i>
                        </div>
                        Ver detalhes
                    </a>
                </div>
                <div class="space-y-3">
                    <p class="text-sm text-neutral-400 font-medium">Accent Rounded (App)</p>
                    <button class="bg-[#ccf32f] hover:bg-[#bce325] text-black font-medium py-3 px-6 rounded-xl transition-colors text-sm w-max">
                        Iniciar Aula
                    </button>
                </div>
                <div class="space-y-3">
                    <p class="text-sm text-neutral-400 font-medium">Dark Rounded (App)</p>
                    <button class="bg-neutral-800 hover:bg-neutral-700 text-white font-medium py-3 px-6 rounded-xl transition-colors text-sm w-max">
                        Cancelar
                    </button>
                </div>
            </div>
        </div>
        <div>
            <h3 class="text-xl font-medium mb-6">Form Elements</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 p-8 bg-white rounded-3xl border border-neutral-100 max-w-4xl">
                <div>
                    <label class="block text-sm font-medium text-neutral-700 mb-1">Standard Input</label>
                    <input class="w-full px-4 py-3 rounded-xl border border-neutral-200 focus:border-black focus:ring-0 outline-none transition-colors" placeholder="Digite seu nome" type="text" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-neutral-700 mb-1">Standard Select</label>
                    <select class="w-full px-4 py-3 rounded-xl border border-neutral-200 focus:border-black focus:ring-0 outline-none transition-colors bg-white">
                        <option value="">Selecione uma opção</option>
                    </select>
                </div>
                <div class="md:col-span-2">
                    <label class="block text-sm font-medium text-neutral-700 mb-2">Radio Selection Cards</label>
                    <div class="grid grid-cols-2 gap-4">
                        <label class="cursor-pointer">
                            <input checked class="peer sr-only" name="profile_ds" type="radio" value="1"/>
                            <div class="border-2 border-neutral-200 rounded-xl p-4 text-center peer-checked:border-black peer-checked:bg-neutral-50 transition-all">
                                <i class="w-6 h-6 mx-auto mb-2 text-neutral-400 peer-checked:text-black" data-lucide="star"></i>
                                <span class="block text-sm font-medium">Option Active</span>
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input class="peer sr-only" name="profile_ds" type="radio" value="2"/>
                            <div class="border-2 border-neutral-200 rounded-xl p-4 text-center peer-checked:border-black peer-checked:bg-neutral-50 transition-all">
                                <i class="w-6 h-6 mx-auto mb-2 text-neutral-400 peer-checked:text-black" data-lucide="circle"></i>
                                <span class="block text-sm font-medium">Option Inactive</span>
                            </div>
                        </label>
                    </div>
                </div>
            </div>
        </div>
        <div>
            <h3 class="text-xl font-medium mb-6">Cards & Containers</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-neutral-50 rounded-[2.5rem] p-10 border border-neutral-100">
                    <div class="flex items-center gap-4 mb-8">
                        <div class="w-14 h-14 rounded-full bg-black text-white flex items-center justify-center">
                            <i class="w-7 h-7" data-lucide="credit-card"></i>
                        </div>
                        <h3 class="text-2xl font-medium">Light Profile Card</h3>
                    </div>
                    <ul class="space-y-6">
                        <li class="flex gap-4 items-start">
                            <div class="mt-1 bg-[#ccf32f] rounded-full p-1"><i class="w-3 h-3 text-black" data-lucide="check"></i></div>
                            <div>
                                <h4 class="font-medium text-lg">List item title</h4>
                                <p class="text-neutral-500 mt-1">This is an example of a list item description inside the card.</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="bg-black text-white rounded-[2.5rem] p-10 border border-neutral-800 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-64 h-64 bg-[#ccf32f] opacity-10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
                    <div class="flex items-center gap-4 mb-8 relative z-10">
                        <div class="w-14 h-14 rounded-full bg-[#ccf32f] text-black flex items-center justify-center">
                            <i class="w-7 h-7" data-lucide="briefcase"></i>
                        </div>
                        <h3 class="text-2xl font-medium">Dark Profile Card</h3>
                    </div>
                    <ul class="space-y-6 relative z-10">
                        <li class="flex gap-4 items-start">
                            <div class="mt-1 bg-[#ccf32f]/20 text-[#ccf32f] rounded-full p-1"><i class="w-3 h-3" data-lucide="check"></i></div>
                            <div>
                                <h4 class="font-medium text-lg">List item title</h4>
                                <p class="text-neutral-400 mt-1">This is an example of a list item description inside the card.</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="bg-white rounded-[2rem] p-8 relative overflow-hidden group hover:shadow-xl transition-all duration-300 border border-neutral-100 col-span-1 md:col-span-2 w-full max-w-sm">
                    <div class="relative z-10">
                        <span class="text-6xl font-medium text-[#ccf32f]/50 absolute -top-4 -right-4">1</span>
                        <div class="w-12 h-12 bg-black rounded-full flex items-center justify-center mb-6 text-white">
                            <i class="w-6 h-6" data-lucide="smartphone"></i>
                        </div>
                        <h3 class="text-xl font-medium mb-3">Step Hover Card</h3>
                        <p class="text-base text-neutral-500 leading-relaxed">Hover to see the gentle shadow transition that gives interactivity.</p>
                    </div>
                </div>
            </div>
        </div>
        <div>
            <h3 class="text-xl font-medium mb-6">Accordion / FAQ Details</h3>
            <div class="max-w-3xl space-y-4">
                <details class="group bg-neutral-50 p-6 rounded-2xl cursor-pointer" open>
                    <summary class="flex justify-between items-center font-medium list-none">
                        <span>O que é a Resolução Contran 1.020/2025? (Active)</span>
                        <span class="transition group-open:rotate-180"><i class="w-5 h-5" data-lucide="chevron-down"></i></span>
                    </summary>
                    <p class="text-neutral-600 mt-4 text-sm leading-relaxed">É a nova regulamentação que permite que instrutores de trânsito credenciados atuem de forma autônoma.</p>
                </details>
                <details class="group bg-neutral-50 p-6 rounded-2xl cursor-pointer">
                    <summary class="flex justify-between items-center font-medium list-none">
                        <span>Como funciona o aluguel da frota? (Inactive)</span>
                        <span class="transition group-open:rotate-180"><i class="w-5 h-5" data-lucide="chevron-down"></i></span>
                    </summary>
                    <p class="text-neutral-600 mt-4 text-sm leading-relaxed">Exemplo de texto escondido sob uma toggle list para poupar espaço.</p>
                </details>
            </div>
        </div>
    </div>
</section>

<section id="layout" class="max-w-7xl mx-auto px-6 py-24 border-b border-neutral-100">
    <div class="mb-16">
        <h2 class="text-3xl md:text-5xl font-medium tracking-tight">4. Layout & Spacing</h2>
        <p class="text-lg text-neutral-500 mt-4 max-w-2xl">Common structural patterns used to align content.</p>
    </div>
    <div class="space-y-16">
        <div>
            <h3 class="text-xl font-medium mb-4">Base Container</h3>
            <div class="p-4 bg-neutral-100 rounded-xl">
                <div class="max-w-7xl mx-auto px-6 py-4 bg-[#ccf32f]/20 border border-[#ccf32f] rounded flex items-center justify-center text-sm font-medium">
                    max-w-7xl mx-auto px-6
                </div>
            </div>
        </div>
        <div>
            <h3 class="text-xl font-medium mb-4">2-Column Grid Pattern (gap-x-12 gap-y-12)</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-12">
                <div class="bg-neutral-100 rounded-xl p-8 flex items-center justify-center text-sm font-medium h-32">Col 1</div>
                <div class="bg-neutral-100 rounded-xl p-8 flex items-center justify-center text-sm font-medium h-32">Col 2</div>
            </div>
        </div>
        <div>
            <h3 class="text-xl font-medium mb-4">3-Column Grid Pattern (gap-8)</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-neutral-100 rounded-xl p-8 flex items-center justify-center text-sm font-medium h-32">Card 1</div>
                <div class="bg-neutral-100 rounded-xl p-8 flex items-center justify-center text-sm font-medium h-32">Card 2</div>
                <div class="bg-neutral-100 rounded-xl p-8 flex items-center justify-center text-sm font-medium h-32">Card 3</div>
            </div>
        </div>
    </div>
</section>

<section id="motion" class="max-w-7xl mx-auto px-6 py-24 border-b border-neutral-100">
    <div class="mb-16">
        <h2 class="text-3xl md:text-5xl font-medium tracking-tight">5. Motion & Interaction</h2>
        <p class="text-lg text-neutral-500 mt-4 max-w-2xl">Transitions and interactive states for elements.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="p-8 border border-neutral-100 rounded-3xl text-center space-y-4">
            <h4 class="font-medium">Button Scale</h4>
            <button class="bg-black text-white text-base font-medium px-7 py-3 rounded-full hover:scale-105 transition-transform mx-auto block">
                Hover Me
            </button>
            <p class="text-xs text-neutral-400">hover:scale-105 transition-transform</p>
        </div>
        <div class="p-8 border border-neutral-100 rounded-3xl text-center space-y-4 bg-neutral-50 group hover:shadow-xl transition-all duration-300">
            <h4 class="font-medium">Card Elevation</h4>
            <div class="p-4 bg-white rounded-xl">
                Hover the card
            </div>
            <p class="text-xs text-neutral-400">hover:shadow-xl transition-all duration-300</p>
        </div>
        <div class="p-8 border border-neutral-100 rounded-3xl text-center space-y-4 flex flex-col items-center justify-center">
            <h4 class="font-medium">Selection Ring</h4>
            <input type="text" class="px-4 py-2 border rounded focus:border-black focus:ring-0 outline-none transition-colors w-full bg-neutral-50" placeholder="Click to focus" />
            <p class="text-xs text-neutral-400">focus:border-black transition-colors</p>
        </div>
    </div>
</section>

<section id="icons" class="max-w-7xl mx-auto px-6 py-24">
    <div class="mb-16">
        <h2 class="text-3xl md:text-5xl font-medium tracking-tight">6. Icons</h2>
        <p class="text-lg text-neutral-500 mt-4 max-w-2xl">Lucide icon set, using standard classes for sizing.</p>
    </div>
    <div class="space-y-12">
        <div>
            <h3 class="text-xl font-medium mb-6">Icon Sizes</h3>
            <div class="flex items-end gap-8 bg-neutral-50 p-8 rounded-3xl border border-neutral-100 w-max">
                <div class="text-center">
                    <i class="w-4 h-4 mx-auto mb-2" data-lucide="star"></i>
                    <div class="text-xs text-neutral-400">w-4 h-4<br/>(16px)</div>
                </div>
                <div class="text-center">
                    <i class="w-5 h-5 mx-auto mb-2" data-lucide="star"></i>
                    <div class="text-xs text-neutral-400">w-5 h-5<br/>(20px)</div>
                </div>
                <div class="text-center">
                    <i class="w-6 h-6 mx-auto mb-2" data-lucide="star"></i>
                    <div class="text-xs text-neutral-400">w-6 h-6<br/>(24px)</div>
                </div>
                <div class="text-center">
                    <i class="w-7 h-7 mx-auto mb-2" data-lucide="star"></i>
                    <div class="text-xs text-neutral-400">w-7 h-7<br/>(28px)</div>
                </div>
                <div class="text-center">
                    <i class="w-10 h-10 mx-auto mb-2" data-lucide="star"></i>
                    <div class="text-xs text-neutral-400">w-10 h-10<br/>(40px)</div>
                </div>
            </div>
        </div>
        <div>
            <h3 class="text-xl font-medium mb-6">Library Sample</h3>
            <div class="grid grid-cols-4 sm:grid-cols-8 gap-4 bg-white p-8 border border-neutral-100 rounded-3xl">
                <div class="flex justify-center p-4"><i class="w-6 h-6" data-lucide="bird"></i></div>
                <div class="flex justify-center p-4"><i class="w-6 h-6" data-lucide="car-front"></i></div>
                <div class="flex justify-center p-4"><i class="w-6 h-6" data-lucide="clipboard-list"></i></div>
                <div class="flex justify-center p-4"><i class="w-6 h-6" data-lucide="info"></i></div>
                <div class="flex justify-center p-4"><i class="w-6 h-6" data-lucide="smartphone"></i></div>
                <div class="flex justify-center p-4"><i class="w-6 h-6" data-lucide="briefcase"></i></div>
                <div class="flex justify-center p-4"><i class="w-6 h-6" data-lucide="graduation-cap"></i></div>
                <div class="flex justify-center p-4"><i class="w-6 h-6" data-lucide="chevron-down"></i></div>
            </div>
        </div>
    </div>
</section>
"""

with open('design-system.html', 'w', encoding='utf-8') as f:
    f.write(head_nav + '\n<main class="w-full overflow-hidden">\n' + hero + '\n' + extra_sections + '\n</main>\n' + footer)

print("Generated design-system.html successfully.")
