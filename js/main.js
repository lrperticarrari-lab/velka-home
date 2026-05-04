// Initialize Lucide Icons
        lucide.createIcons();

        // Setup GSAP & Lenis
        gsap.registerPlugin(ScrollTrigger);

        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            direction: 'vertical',
            smooth: true,
        });
        function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);

        // Navbar blur/solid effect on scroll
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Split text for animation
        document.querySelectorAll('.split-animate').forEach(el => {
            const text = el.innerText;
            const words = text.split(' ');
            el.innerHTML = '';
            words.forEach(word => {
                const wordWrap = document.createElement('span');
                wordWrap.classList.add('word-wrap');
                wordWrap.innerHTML = `<span class="word-inner">${word}&nbsp;</span>`;
                el.appendChild(wordWrap);
            });
        });

        // Initial Load Animations
        window.addEventListener('DOMContentLoaded', () => {
            document.body.style.opacity = 1;

            const tl = gsap.timeline({ delay: 0.2 }); // 200ms delay requested

            // Text split reveal
            tl.to('.word-inner', {
                y: "0%",
                duration: 1.2,
                ease: "power4.out",
                stagger: 0.05
            });

            // Fade in paragraphs, buttons, and decorative elements
            tl.to('.hero-fade', {
                opacity: 1,
                y: 0,
                duration: 1,
                stagger: 0.15,
                ease: "power3.out"
            }, "-=0.8");

            // GSAP MatchMedia for Performance Optimization
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
            });

            // Mothers Day Carousel Logic
            const carousel = document.getElementById('mothersDayCarousel');
            const btnPrev = document.getElementById('btnPrev');
            const btnNext = document.getElementById('btnNext');
            const dots = document.querySelectorAll('.carousel-dot');

            if (carousel && btnNext && btnPrev) {
                const updateDots = () => {
                    const index = Math.round(carousel.scrollLeft / carousel.clientWidth);
                    dots.forEach((dot, i) => {
                        dot.style.opacity = i === index ? '1' : '0.4';
                    });
                };

                btnNext.addEventListener('click', () => {
                    carousel.scrollBy({ left: carousel.clientWidth, behavior: 'smooth' });
                });

                btnPrev.addEventListener('click', () => {
                    carousel.scrollBy({ left: -carousel.clientWidth, behavior: 'smooth' });
                });
                
                dots.forEach((dot, index) => {
                    dot.addEventListener('click', () => {
                        carousel.scrollTo({ left: carousel.clientWidth * index, behavior: 'smooth' });
                    });
                });

                carousel.addEventListener('scroll', updateDots);
                window.addEventListener('resize', updateDots);
            }

            // Kits Essenciais Carousel Logic
            const kitsCarousel = document.getElementById('kitsCarouselContainer');
            const kitsPrev = document.getElementById('kitsPrev');
            const kitsNext = document.getElementById('kitsNext');

            if (kitsCarousel && kitsNext && kitsPrev) {
                kitsNext.addEventListener('click', () => {
                    kitsCarousel.scrollBy({ left: kitsCarousel.clientWidth / 2, behavior: 'smooth' });
                });

                kitsPrev.addEventListener('click', () => {
                    kitsCarousel.scrollBy({ left: -(kitsCarousel.clientWidth / 2), behavior: 'smooth' });
                });
            }
        });

document.addEventListener('DOMContentLoaded', () => {
            const lancamentosCarousel = document.getElementById('lancamentosCarouselContainer');
            const lancamentosPrev = document.getElementById('lancamentosPrev');
            const lancamentosNext = document.getElementById('lancamentosNext');

            if (lancamentosCarousel && lancamentosPrev && lancamentosNext) {
                lancamentosNext.addEventListener('click', () => {
                    lancamentosCarousel.scrollBy({ left: 300, behavior: 'smooth' });
                });
                lancamentosPrev.addEventListener('click', () => {
                    lancamentosCarousel.scrollBy({ left: -300, behavior: 'smooth' });
                });
            }
        });


        document.addEventListener('DOMContentLoaded', () => {
            const maisVendidosCarousel = document.getElementById('maisVendidosCarouselContainer');
            const maisVendidosPrev = document.getElementById('maisVendidosPrev');
            const maisVendidosNext = document.getElementById('maisVendidosNext');

            if (maisVendidosCarousel && maisVendidosPrev && maisVendidosNext) {
                maisVendidosNext.addEventListener('click', () => {
                    maisVendidosCarousel.scrollBy({ left: 320, behavior: 'smooth' });
                });
                maisVendidosPrev.addEventListener('click', () => {
                    maisVendidosCarousel.scrollBy({ left: -320, behavior: 'smooth' });
                });
            }

            const categoriasCarousel = document.getElementById('categoriasCarouselContainer');
            const categoriasPrev = document.getElementById('categoriasPrev');
            const categoriasNext = document.getElementById('categoriasNext');

            if (categoriasCarousel && categoriasPrev && categoriasNext) {
                categoriasNext.addEventListener('click', () => {
                    categoriasCarousel.scrollBy({ left: 320, behavior: 'smooth' });
                });
                categoriasPrev.addEventListener('click', () => {
                    categoriasCarousel.scrollBy({ left: -320, behavior: 'smooth' });
                });
            }

            // Mobile Menu Logic
            const mobileMenuBtn = document.getElementById('mobileMenuBtn');
            const mobileMenu = document.getElementById('mobileMenu');
            if (mobileMenuBtn && mobileMenu) {
                const mobileMenuIcon = mobileMenuBtn.querySelector('i');
                let isMenuOpen = false;

                mobileMenuBtn.addEventListener('click', () => {
                    isMenuOpen = !isMenuOpen;
                    if (isMenuOpen) {
                        mobileMenu.classList.remove('translate-x-full');
                        mobileMenu.classList.add('translate-x-0');
                        if (mobileMenuIcon) mobileMenuIcon.setAttribute('data-lucide', 'x');
                        lucide.createIcons();
                        document.body.style.overflow = 'hidden';
                    } else {
                        mobileMenu.classList.remove('translate-x-0');
                        mobileMenu.classList.add('translate-x-full');
                        if (mobileMenuIcon) mobileMenuIcon.setAttribute('data-lucide', 'menu');
                        lucide.createIcons();
                        document.body.style.overflow = '';
                    }
                });
                
                // Close menu when clicking a link
                const mobileLinks = mobileMenu.querySelectorAll('.mobile-link');
                mobileLinks.forEach(link => {
                    link.addEventListener('click', () => {
                        isMenuOpen = false;
                        mobileMenu.classList.remove('translate-x-0');
                        mobileMenu.classList.add('translate-x-full');
                        if (mobileMenuIcon) mobileMenuIcon.setAttribute('data-lucide', 'menu');
                        lucide.createIcons();
                        document.body.style.overflow = '';
                    });
                });
            }
        });
