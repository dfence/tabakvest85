// Tabakvest 85 - Main JavaScript

// Add active nav link highlighting
document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === 'index.html' || link.getAttribute('href') === './') {
            if (currentPath.endsWith('index.html') || currentPath.endsWith('/')) {
                link.classList.add('active');
            }
        }
    });

    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('nav ul');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close menu when a link is clicked
        const navLinks = document.querySelectorAll('nav ul a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!event.target.closest('nav')) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }
});

// Handle nav scroll effect - add dark background when scrolling
window.addEventListener('scroll', function() {
    const nav = document.querySelector('nav');
    if (window.scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});

// Mobile menu toggle (for future mobile menu implementation)
function toggleMobileMenu() {
    const nav = document.querySelector('nav ul');
    if (nav) {
        nav.style.display = nav.style.display === 'none' ? 'flex' : 'none';
    }
}

// Initialize SimpleLightbox for gallery images
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('[data-glightbox]');
    if (images.length > 0 && typeof SimpleLightbox !== 'undefined') {
        new SimpleLightbox('[data-glightbox]');
        console.log(`SimpleLightbox initialized with ${images.length} images`);
    }
});
