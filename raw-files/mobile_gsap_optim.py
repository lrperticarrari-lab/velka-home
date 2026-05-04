import re

with open('js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Define the target block to replace
target_block = """            // Hero image subtle zoom out (Parallax setup)
            gsap.to('.hero-img', {
                yPercent: 15,
                ease: "none",
                scrollTrigger: {
                    trigger: ".hero-img",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }
            });

            // General Reveal Up Elements for scroll
            const revealElements = document.querySelectorAll('.reveal-up');
            revealElements.forEach(el => {
                gsap.fromTo(el, 
                    { opacity: 0, y: 30, filter: "blur(10px)" },
                    {
                        opacity: 1,
                        y: 0,
                        filter: "blur(0px)",
                        duration: 1.2,
                        ease: "power3.out",
                        scrollTrigger: {
                            trigger: el,
                            start: "top 85%",
                            toggleActions: "play none none reverse"
                        }
                    }
                );
            });"""

new_block = """            // GSAP MatchMedia for Performance Optimization
            let mm = gsap.matchMedia();

            mm.add("(min-width: 768px)", () => {
                // Desktop: Full parallax and blur reveals
                gsap.to('.hero-img', {
                    yPercent: 15,
                    ease: "none",
                    scrollTrigger: {
                        trigger: ".hero-img",
                        start: "top top",
                        end: "bottom top",
                        scrub: true
                    }
                });

                const revealElements = document.querySelectorAll('.reveal-up');
                revealElements.forEach(el => {
                    gsap.fromTo(el, 
                        { opacity: 0, y: 30, filter: "blur(10px)" },
                        {
                            opacity: 1,
                            y: 0,
                            filter: "blur(0px)",
                            duration: 1.2,
                            ease: "power3.out",
                            scrollTrigger: {
                                trigger: el,
                                start: "top 85%",
                                toggleActions: "play none none reverse"
                            }
                        }
                    );
                });
            });

            mm.add("(max-width: 767px)", () => {
                // Mobile: Simplified animations (no parallax, no blur, faster)
                const revealElements = document.querySelectorAll('.reveal-up');
                revealElements.forEach(el => {
                    gsap.fromTo(el, 
                        { opacity: 0, y: 15 },
                        {
                            opacity: 1,
                            y: 0,
                            duration: 0.6,
                            ease: "power2.out",
                            scrollTrigger: {
                                trigger: el,
                                start: "top 92%",
                                toggleActions: "play none none none"
                            }
                        }
                    );
                });
            });"""

if target_block in js_content:
    js_content = js_content.replace(target_block, new_block)
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("JS animations updated successfully.")
else:
    print("Could not find the target block in main.js")

