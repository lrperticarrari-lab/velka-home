import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s3_start = content.find("<!-- SECTION 3: MAIS VENDIDOS -->")
s4_start = content.find("<!-- SECTION 4: CARROSSEL DIA DAS MÃES -->")

if s3_start != -1 and s4_start != -1:
    s3_content = content[s3_start:s4_start]

    # 1. Outer product card
    # Change: <div class="group cursor-hover">
    # To: <div class="group cursor-hover relative flex flex-col p-3 rounded-3xl transition-all duration-700 hover:-translate-y-3 hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)] bg-transparent hover:bg-white border border-transparent hover:border-dark/5">
    s3_content = s3_content.replace('<div class="group cursor-hover">', '<div class="group cursor-hover relative flex flex-col p-3 rounded-3xl transition-all duration-700 hover:-translate-y-3 hover:shadow-[0_20px_40px_-15px_rgba(0,0,0,0.08)] bg-transparent hover:bg-white border border-transparent hover:border-dark/5">')

    # 2. Inner image container
    # Change: <div class="w-full aspect-square bg-white relative overflow-hidden flex items-center justify-center mb-4 p-4 border border-dark/5">
    # To: <div class="w-full aspect-square bg-stone relative overflow-hidden flex items-center justify-center mb-5 p-6 rounded-2xl border border-transparent group-hover:bg-white transition-colors duration-500">
    s3_content = s3_content.replace('<div class="w-full aspect-square bg-white relative overflow-hidden flex items-center justify-center mb-4 p-4 border border-dark/5">', '<div class="w-full aspect-square bg-stone relative overflow-hidden flex items-center justify-center mb-5 p-6 rounded-2xl border border-transparent group-hover:bg-white transition-colors duration-500">')

    # 3. Main image hover animation
    # Change: group-hover:scale-105 transition-transform duration-500
    # To: group-hover:scale-110 group-hover:-translate-y-2 transition-all duration-[800ms] ease-[cubic-bezier(0.25,1,0.5,1)]
    s3_content = s3_content.replace('group-hover:scale-105 transition-transform duration-500', 'group-hover:scale-110 group-hover:-translate-y-2 transition-all duration-[800ms] ease-[cubic-bezier(0.25,1,0.5,1)]')

    # 4. Thumbnails dock
    # Change: opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-white/80 backdrop-blur-md p-1.5 rounded-xl z-20 shadow-lg
    # To: opacity-0 translate-y-4 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-[600ms] ease-[cubic-bezier(0.16,1,0.3,1)] bg-white/80 backdrop-blur-xl border border-white/60 p-2 rounded-2xl z-20 shadow-[0_8px_30px_rgb(0,0,0,0.08)]
    s3_content = s3_content.replace('opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-white/80 backdrop-blur-md p-1.5 rounded-xl z-20 shadow-lg', 'opacity-0 translate-y-4 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-[600ms] ease-[cubic-bezier(0.16,1,0.3,1)] bg-white/80 backdrop-blur-xl border border-white/60 p-2 rounded-2xl z-20 shadow-[0_8px_30px_rgb(0,0,0,0.08)]')

    # 5. Price and Bag button
    # Add a slight hover effect on the bag button container text-dark/50 to text-dark
    s3_content = s3_content.replace('text-dark/50 hover:text-accent transition-colors', 'w-10 h-10 flex items-center justify-center rounded-full bg-stone text-dark/60 hover:bg-dark hover:text-white transition-all duration-300 hover:scale-110')
    
    # Also fix the grid layout gap from 6 to 4 or 6, it's 6 already.
    # We will add an stagger to the grid if possible. But they are all in one reveal-up container.

    # Reconstruct the file
    new_content = content[:s3_start] + s3_content + content[s4_start:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated Dobra 3.")
else:
    print("Markers not found.")
