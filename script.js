// Mobile menu toggle
const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');

if (menuToggle && mobileMenu) {
  menuToggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('show');
  });
}

// Smooth scrolling for all anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
      // Close mobile menu if open
      if (mobileMenu) mobileMenu.classList.remove('show');
    }
  });
});

// Close mobile menu on window resize (if opened and screen becomes large)
window.addEventListener('resize', () => {
  if (window.innerWidth > 968 && mobileMenu) {
    mobileMenu.classList.remove('show');
  }
});