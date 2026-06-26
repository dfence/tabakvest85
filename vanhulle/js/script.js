// Mobile menu toggle
const hamburger = document.querySelector('.hamburger');
const navUl = document.querySelector('nav ul');
const navLinks = document.querySelectorAll('nav ul li a');

if (hamburger) {
  hamburger.addEventListener('click', () => {
    navUl.classList.toggle('active');
  });

  // Close menu when a link is clicked
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navUl.classList.remove('active');
    });
  });
}

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('nav')) {
    navUl?.classList.remove('active');
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    if (href !== '#' && document.querySelector(href)) {
      e.preventDefault();
      document.querySelector(href).scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Active nav link on scroll
window.addEventListener('scroll', () => {
  let current = '';
  
  const sections = document.querySelectorAll('section, header');
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= sectionTop - 200) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current || (current === '' && link.getAttribute('href') === 'index.html')) {
      link.classList.add('active');
    }
  });
});
