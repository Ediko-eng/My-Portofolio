const body = document.body;
const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');
const themeToggle = document.getElementById('themeToggle');
const themeIcon = themeToggle ? themeToggle.querySelector('i') : null;

const applyTheme = (theme) => {
  const selectedTheme = theme === 'light' ? 'light' : 'dark';
  body.setAttribute('data-theme', selectedTheme);
  if (themeIcon) {
    themeIcon.classList.toggle('fa-moon', selectedTheme === 'dark');
    themeIcon.classList.toggle('fa-sun', selectedTheme === 'light');
  }
  localStorage.setItem('portfolio-theme', selectedTheme);
};

const currentTheme = localStorage.getItem('portfolio-theme');
applyTheme(currentTheme || 'dark');

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const nextTheme = body.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    applyTheme(nextTheme);
  });
}

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
      if (mobileMenu) mobileMenu.classList.remove('show');
    }
  });
});

window.addEventListener('resize', () => {
  if (window.innerWidth > 968 && mobileMenu) {
    mobileMenu.classList.remove('show');
  }
});
