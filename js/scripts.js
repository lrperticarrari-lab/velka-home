// Optional Lançamentos Carousel Logic
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
