// Smooth Scrolling Function
document.querySelectorAll('.nav-link').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Initialize AOS (Animate on Scroll)
AOS.init({
    duration: 1200,
    once: true,
    easing: 'ease-in-out',
});
